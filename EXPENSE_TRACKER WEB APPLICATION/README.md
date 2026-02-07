# 💰 Expense Tracker – Django Web Application

The **Expense Tracker** is a web-based application developed using the **Django framework** that helps users manage and analyze their daily expenses.  
It allows users to record expenses, view monthly summaries, and analyze category-wise spending through a clean and responsive interface.

---

##  Features

- Secure user authentication
- Add, view, edit, and delete expenses
- User-specific expense management
- Monthly total expense calculation
- Category-wise expense summary
- Responsive user interface using Bootstrap
- Admin panel for managing expense data

---

##  Tech Stack

### Frontend
- HTML5  
- CSS3  
- Bootstrap 5  

### Backend
- Django (Python Framework)  
- Django ORM  

### Database
- SQLite  

### Architecture
- MVT (Model–View–Template)


---

## 📊 Application Modules

### Authentication Module
- Login-based access control
- Each user can view and manage only their own expenses

### Expense Management Module
- Create new expense records
- View existing expenses
- Update expense details
- Delete expenses

### Expense Analytics Module
- Monthly total expense calculation
- Category-wise expense aggregation

###  Admin Module
- Admin dashboard for managing all expense records
- Filtering and searching functionality

---

##  Screenshots

### Expense Dashboard
![Expense Dashboard](https://github.com/deepantikajain/Python-Projects/blob/main/EXPENSE_TRACKER%20WEB%20APPLICATION/dashboard.png?raw=true)

### Add / Edit Expense
![Add Expense](https://github.com/deepantikajain/Python-Projects/blob/main/EXPENSE_TRACKER%20WEB%20APPLICATION/add_expense.png?raw=true)

### Admin Panel
![Admin Panel](https://github.com/deepantikajain/Python-Projects/blob/main/EXPENSE_TRACKER%20WEB%20APPLICATION/admin.png?raw=true)

>  *All screenshots are placed inside the `screenshots/` folder.*

---
##  Project Structure

``` expense_tracker/
│
├── manage.py
│
├── static/
│ └── css/
│ └── style.css
│
├── templates/
│ ├── base.html
│ ├── expense_list.html
│ └── expense_form.html
│
├── expenses/
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── admin.py
│ └── urls.py
│
├── expense_tracker/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py ```

## 🧾 Conclusion

The **Expense Tracker Web Application** demonstrates practical implementation of Django concepts such as authentication, CRUD operations, ORM-based database handling, and template inheritance.  
The project provides a simple yet effective solution for personal expense management and serves as a strong foundation for advanced web development projects.



