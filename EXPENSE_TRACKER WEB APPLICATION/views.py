from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date

from .models import Expense
from .forms import ExpenseForm


# READ + ANALYTICS (List expenses, monthly total, category-wise total)
@login_required
def expense_list(request):
    today = date.today()

    expenses = Expense.objects.filter(
        user=request.user,
        date__month=today.month,
        date__year=today.year
    )

    total_monthly = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    category_totals = expenses.values('category').annotate(
        total=Sum('amount')
    )

    context = {
        'expenses': expenses,
        'total_monthly': total_monthly,
        'category_totals': category_totals,
    }

    return render(request, 'expense_list.html', context)


# CREATE (Add expense)
@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'expense_form.html', {'form': form})


# UPDATE (Edit expense)
@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expense_form.html', {'form': form})


# DELETE (Delete expense)
@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    expense.delete()
    return redirect('expense_list')
