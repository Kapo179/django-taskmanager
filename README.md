# Django Kanban: Task Management App

Easily organize and manage your tasks with this Django-based Kanban application.

## Key Features

- **User Authentication**: Secure user login and personalized task management using Django's authentication system.

- **Task Management (CRUD)**: Add, edit, and delete tasks effortlessly with full Create, Read, Update, and Delete functionality.

- **Kanban Board View**: Visualize your tasks across customizable categories such as To Do, In Progress, and Done.

- **Task Status Updates**: Drag and drop tasks to update their status between columns in real-time.

- **Responsive Design**: Optimized for desktops and mobile devices, ensuring seamless usage across screen sizes.

- **Clean and Intuitive Interface**: Simple design makes task organization and navigation straightforward and efficient.

## Figma Wireframe Mockup

**Overview**

- The Landing website mockup, focuses on providing the user with a demo kanban board, to allow interaction before building their own board.
- The Second page is the intended simple, main app page. Simplified to not overwhelm the user, and sticks to the theme adopted within the website mockup. This could change in the future

![Frame 2 (1)](https://github.com/user-attachments/assets/bc4272ec-4775-4fdc-a0a1-a611cbbff29e)
![Frame 3](https://github.com/user-attachments/assets/a3bce156-90a5-42a7-b8eb-0c89bf70e761)

## Typography
- SF Compact Display 
( For H2 - Font-weight: 600 )
- SF Compact Display - Bold for H1

We settled with SF Compact Display, It is an Apple system font therefore I need to remain cautious about my usage.

As you can see, my styling and usage of the font, replicates my mock-up well. (Mockup Above)
![image](https://github.com/user-attachments/assets/57a98c8c-8b80-4879-a697-859a70931557)





## Data Structure

**Below is our proposed Entity Relationship Diagram which will be intended to be kept straight forward.**

![Untitled (2)](https://github.com/user-attachments/assets/e3e3791f-60eb-4899-bf8a-1a218a78ed63)

## Inspiration

**Below is the initial inspiration, which shows the kanban board design used by monday.com** 

![image](https://github.com/user-attachments/assets/484e76aa-b358-4e88-99ac-2092830f3f2f)

## AI Usage 

**Example of AI Support**

- I hit a roadblock in which i accidentally pushed another repo from within this project, and I needed to undo this without destroying my django model.

![image](https://github.com/user-attachments/assets/508a387c-19fb-4093-92fe-9849e7702d57)


## Testing

To run all tests:
   python manage.py test

To run tests for the Boards app only:
   python manage.py test boards

In our initial tests of our models, we've documented our test which reviewed task association to the user, as well as task creation functionality for authenticated and non-authenticated users.

**To run these tests yourself:**

Ensure you have navigate to 'cd taskmanager' (If you are already in /django-taskmanager, do this)

Then run python manage.py test boards.tests.test_views (This will test taskmanager/boards/tests/test_views.py)

If you like to test (taskmanager/boards/test/test_views.py), run python manage.py test boards.tests.tests

![image](https://github.com/user-attachments/assets/917f62e2-a32d-477e-bc94-5889a560b5f8)

![image](https://github.com/user-attachments/assets/a7129314-ff9b-42b9-a1a6-34a0adc98cc1)

## Mockup Replication Attempt

**Modal Design**

The initial modal designed by me, was not styled as well as I'd like it to turn out.
![image](https://github.com/user-attachments/assets/3121cef7-0672-422c-925e-0ca5f40cae35)

Therefore I found a modal design online which used tailwindcss

![image](https://github.com/user-attachments/assets/3d02d09b-cd5f-41a3-8440-f2480dd19e6d)

The end result, drastically improved the modal design.

![image](https://github.com/user-attachments/assets/a266726b-dcd8-49db-b29a-9a92d311759c)

