from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    due_date = db.Column(db.String(20), nullable=True)
    status = db.Column(db.String(20), default="Pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"

# Home (Create + Read)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        due_date = request.form.get('due_date')

        new_task = Todo(task=task, due_date=due_date)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

    tasks = Todo.query.order_by(Todo.created_at).all()
    return render_template('index.html', tasks=tasks)

# Update Task
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.task = request.form['task']
        task.due_date = request.form.get('due_date')
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('update.html', task=task)

# Delete Task
@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# Toggle Status
@app.route('/status/<int:id>')
def status(id):
    task = Todo.query.get_or_404(id)
    task.status = "Completed" if task.status == "Pending" else "Pending"
    db.session.commit()
    return redirect(url_for('index'))

# Run App
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
