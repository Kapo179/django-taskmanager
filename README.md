# KanDo
![Frame 1 (2)](https://github.com/user-attachments/assets/0dd97852-2d6d-4205-8591-5dde1c46f69c)


A Django-based productivity application that helps users organize, track, and manage their tasks efficiently, complete with a visually appealing Kanban board and rich text editing for task details.

---

## Table of Contents
1. [User Experience (UX)](#user-experience-ux)
   - [Strategy & Design Goals](#strategy--design-goals)
   - [User Stories](#user-stories)
   - [Information Architecture](#information-architecture)
2. [Features](#features)
   - [Current Features](#current-features)
   - [Screenshots](#screenshots)
   - [Future Features](#future-features)
3. [Agile Process](#agile-process)
4. [Testing](#testing)
   - [Automated Tests](#automated-tests)
   - [Manual Testing & Screenshots](#manual-testing--screenshots)
   - [Known Bugs & Resolutions](#known-bugs--resolutions)
5. [Deployment](#deployment)
6. [Credits](#credits)
   - [Code & Resources](#code--resources)
   - [Special Thanks](#special-thanks)
7. [License](#license)

---

## User Experience (UX)

### Strategy & Design Goals
- **Intuitive Task Management**: Allow users to quickly create, update, and track tasks without confusion.
- **Modern Minimal design Practices: Utilising professionally designed.

- The Page is the intended simple, main app page. Simplified to not overwhelm the user, and sticks to the theme adopted within the website mockup. 

![Frame 3](https://github.com/user-attachments/assets/a3bce156-90a5-42a7-b8eb-0c89bf70e761)

## Typography
SF Compact Display 
- ( For H1, H2, - Font-weight: 700 )
- ( For H3, H4, H5 - Font-weight: 500)
- ( For H3, H4, H5 - Font-weight: 400)

## Colour Pallette
Kanban Colour Usage
- ( #838383 - For Not Started UI | #747577- Font colour )
- ( #F0E7F6 - For Doing Title UI | #7B777E - Font colour  )
- ( #FFDCE0 - For Done Title UI | #837173 - Font colour  )
- ( #FFFFFF & #DDDDDD {Border Strokes} - For Card UI, e.g: Kanban Cards, Registration or New Task Modals )
- ( #F3F4F4 Column Background )
- ( #CBDFD8 - Slightly Important Tag | #68736F - Font colour )
- ( #FFDCE0 - Urgent Tag | #837173 - Font colour )

We settled with SF Compact Display, It is an Apple system font therefore I need to remain cautious about my usage.

As you can see, my styling and usage of the font, replicates my mock-up well. (Mockup Above)
![image](https://github.com/user-attachments/assets/57a98c8c-8b80-4879-a697-859a70931557)

Here's the final Look

![image](https://github.com/user-attachments/assets/f5f2c789-6d62-498b-ac32-ee0f4bcb110a)



- **Visual Clarity**: Present tasks in a Kanban board layout so users see their workflow at a glance.
- **Responsive & Accessible**: Ensure that users can manage tasks across devices of varying screen sizes.

### User Stories
Below are example user stories illustrating how different users engage with the app:

1. **New User**:  
   *“As a new user, I want to easily sign up and set up my first task so I can start tracking my work right away.”*

2. **Returning User**:  
   *“As a returning user, I want to view my tasks in a Kanban layout and quickly update their status via drag-and-drop.”*

3. **Consistent User**:  
   *“As a consistent user, I want to use rich text formatting (Quill.js) within a task’s description to add images, links, and bullet points for clarity.”*

### Information Architecture
- **Models**:  
  - **Task** model: holds the title, description, priority, deadlines, etc.  
  - **Project/Board** model (if applicable): categorizes tasks or groups them by domain.  
  - **User** model: authentication and association to tasks.

**Below is our proposed Entity Relationship Diagram which will be intended to be kept straight forward.**

![Untitled (2)](https://github.com/user-attachments/assets/e3e3791f-60eb-4899-bf8a-1a218a78ed63)

**Modal Design**

The initial modal designed by me, was not styled as well as I'd like it to turn out.
![image](https://github.com/user-attachments/assets/3121cef7-0672-422c-925e-0ca5f40cae35)

Therefore I found a modal design online which was styled in a universally accepted format

![image](https://github.com/user-attachments/assets/3d02d09b-cd5f-41a3-8440-f2480dd19e6d)

The end result, drastically improved the modal design.

![image](https://github.com/user-attachments/assets/a266726b-dcd8-49db-b29a-9a92d311759c)

---

## Features

### Current Features
1. **Kanban Board**  
   - Drag-and-drop interface to move tasks between columns (e.g., To Do, In Progress, Done).

2. **Task Priority & Deadline**  
   - Visually tag tasks with priority levels and highlight overdue tasks.

3. **Rich Text Editing**  
   - Powered by [Quill.js](https://quilljs.com/), allowing for formatted descriptions.

4. **Task Details Modal**  
   - Interactive modal to view and edit comprehensive task info, including a timeline for status changes.

5. **Responsiveness & Mobile View**  
   - Adjusts layout for smaller screens and ensures consistent UX.

### Screenshots

1. **Kanban Board View**  
![image](https://github.com/user-attachments/assets/ab43ff5f-d062-413d-be02-acac3c2878cf)


2. **Task Modal with Rich Text Editor**  
   ![Task Modal Screenshot](./assets/task-modal-quill.png)

### Future Features
- **User Activity Feed**: A timeline of changes or updates made to tasks.
- **Search & Filters**: Quick searching or filtering tasks by tag, status, or priority.
- **Reminders/Notifications**: Email or in-app notifications for overdue tasks.

---

## Agile Process

This project follows an Agile approach to development:

- **GitHub Project Board**  
  - [[Link to Agile Board](https://github.com/users/Kapo179/projects/3)](#)  
![image](https://github.com/user-attachments/assets/57a3b40c-1f2f-45c3-8831-85cbd21dc75a)


## Sprints & Milestones

Throughout the project, we followed an Agile methodology, breaking the development process into multiple sprints. Each sprint focused on a specific set of goals, tracked via GitHub issues and integrated via Pull Requests. Below is an overview of our major sprints and the corresponding milestones:

### Sprint 1: Project Setup & Core Models
- **Duration**: 1 week
- **Goals**:
  - Configure Django project skeleton and necessary dependencies.
  - Establish core `Task` and `Project` models.
  - Implement initial user authentication flow using Django’s built-in `User` model.
- **Key Commits**:
  - `[commit-hash]`: **Initialize Django project** with `django-admin startproject`.
  - `[commit-hash]`: **Add Task and Project models** featuring fields for titles, descriptions, due dates, and user associations.
  - `[commit-hash]`: **Set up user login/logout** with custom authentication templates.



### Sprint 2: CRUD Features & Basic UI
- **Duration**: 1 week
- **Goals**:
  - Enable Create, Read, Update, and Delete operations for tasks and projects.
  - Integrate a basic Bootstrap layout for consistent UI/UX.
  - Provide a dashboard displaying upcoming tasks and deadlines.
- **Key Commits**:
  - `[commit-hash]`: **Implement CRUD for tasks** in `views.py` and link templates for list/detail.
  - `[commit-hash]`: **Add Bootstrap** for styling the base templates and form elements.
  - `[commit-hash]`: **Create a dashboard** pulling tasks by due date, assigned user, and status.


### Sprint 3: Kanban Board & Rich Text Editing
- **Duration**: 2 weeks
- **Goals**:
  - Introduce a **drag-and-drop Kanban board** for tasks.
  - Enhance task details with **Quill.js** for rich text descriptions.
  - Establish user stories ensuring both basic and advanced users can quickly interact with tasks.
- **Key Commits**:
  - `[commit-hash]`: **Setup Kanban board** with drag-and-drop columns reflecting task status (To Do, In Progress, Done).
  - `[commit-hash]`: **Integrate Quill.js** enabling formatted task descriptions, images, and links.
  - `[commit-hash]`: **Refactor views** into class-based views for better maintainability and easier updates to Kanban statuses.


### Sprint 4: Testing & Deployment Preparations
- **Duration**: 1 week
- **Goals**:
  - Write **unit tests** for models and views to ensure data integrity and functionality.
  - Add **integration tests** to validate the full user journey (creating a task, updating its status on the Kanban board, etc.).
  - Prepare the project for **deployment** (e.g., on Heroku, Render) with environment variables and static file configuration.
- **Key Commits**:
  - `[commit-hash]`: **Create test_models.py and test_views.py** to cover model logic, form validation, and permission checks.
  - `[commit-hash]`: **Add GitHub Actions** for CI/CD—automatically running tests on pull requests.
  - `[commit-hash]`: **Configure production settings** and deployment instructions in the README.


### Sprint 5: UI Polish, User Feedback & Final Adjustments
- **Duration**: 1 week
- **Goals**:
  - Conduct a UI/UX review and gather user feedback.
  - Optimize mobile responsiveness and fix any known bugs.
  - Finalize **README** with screenshots, testing details, and improved documentation.
- **Key Commits**:
  - `[commit-hash]`: **Enhance mobile layouts** ensuring the Kanban board is scrollable and Quill editor is usable on smaller screens.
  - `[commit-hash]`: **Fix bugs** related to updating task priorities and incomplete drag events on certain browsers.
  - `[commit-hash]`: **Update README** with feature screenshots, test coverage details, and instructions for local setup & deployment.


---

## Testing

### Automated Tests

- **Unit Tests**  
  - `test_models.py`: verifies Task model logic, deadlines, etc.  
  - `test_views.py`: checks view responses, redirects, and permissions.

- **Integration Tests**  

taskmanager/boards/templates/boards/board.html
![image](https://github.com/user-attachments/assets/92f8c0e1-4723-428e-b01b-fa8d3b06113e)

taskmanager/boards/templates/boards/task_detail.html
![image](https://github.com/user-attachments/assets/5304cdf9-39fa-4219-84b1-8c2b0b48943c)



### Manual Testing & Screenshots
- **Browser-Based Checks**  
  - Verified form validations, modal pop-ups, and drag-and-drop functionality in Chrome, Firefox, and mobile browsers.

- **Screenshots**  
taskmanager/accounts/forms.py
![image](https://github.com/user-attachments/assets/afc33e31-fa7c-4e40-bf9d-037c084e5f8a)

taskmanager/accounts/models.py
![image](https://github.com/user-attachments/assets/55c4dc81-cb5d-4d31-aa3e-1aeac1e487de)

taskmanager/accounts/apps.py
![image](https://github.com/user-attachments/assets/744e7d5d-c789-45f2-97c1-f0e50cef2ac7)

taskmanager/accounts/admin.py
![image](https://github.com/user-attachments/assets/d62c5100-63a2-4fa3-b941-5c40befe18e0)


taskmanager/accounts/tests.py
![image](https://github.com/user-attachments/assets/3ad78528-4266-4536-8f95-d57374e7bdd9)

taskmanager/accounts/views.py
![image](https://github.com/user-attachments/assets/b3a95e4c-d167-42be-b564-3763d98815e9)

taskmanager/boards/admin.py
![image](https://github.com/user-attachments/assets/c5cd12b6-a5ca-4310-81e7-f34d24156ecb)

taskmanager/boards/apps.py
![image](https://github.com/user-attachments/assets/59750a96-07b0-46fd-920b-82c7139d5895)

taskmanager/boards/models.py
![image](https://github.com/user-attachments/assets/664dc8e4-aa6d-4831-9e82-5690308e99c4)

taskmanager/boards/test_views.py
![image](https://github.com/user-attachments/assets/892209a4-a409-45d7-bd83-b39b92fce8ac)

taskmanager/boards/tests.py
![image](https://github.com/user-attachments/assets/8a3eadcf-e613-47a3-be3e-ec57bece8ed1)

taskmanager/boards/views.py
![image](https://github.com/user-attachments/assets/942784ee-3079-4a11-810d-5176b67f16a1)

taskmanager/boards/urls.py
![image](https://github.com/user-attachments/assets/0a7874ed-829e-47cd-a99f-6d5db0aa9041)


taskmanager/taskmanager/asgi.py
![image](https://github.com/user-attachments/assets/3b2393d3-9436-4c08-b8bf-d6e427703ab0)

taskmanager/taskmanager/settings.py
![image](https://github.com/user-attachments/assets/c618ebca-2eaf-4fcc-ba9f-be2de6db46f7)

taskmanager/taskmanager/urls.py
![image](https://github.com/user-attachments/assets/171db982-a618-4c11-b94a-b715b76e32f6)

taskmanager/taskmanager/wsgi.py
![image](https://github.com/user-attachments/assets/cd3d01b0-588a-41a6-a3c8-154770d65d39)

taskmanager/manage.py
![image](https://github.com/user-attachments/assets/0ef556e1-eac7-4049-b104-d1df9b27729e)

KanBan View 
![image](https://github.com/user-attachments/assets/2baed5b6-0259-4bc2-83f6-6abc9e3df1cd)

Task Creation Modal View 
![image](https://github.com/user-attachments/assets/210699ad-2257-44c7-8973-51119fe04319)

Text Editor
![image](https://github.com/user-attachments/assets/f33791c8-cbfc-49e1-9345-810b6c57804f)

taskmanager/boards/models.py 
![image](https://github.com/user-attachments/assets/e41570b9-d9ab-4163-9438-10a97a8474fe)

taskmanager/boards/urls.py 
![image](https://github.com/user-attachments/assets/72006eba-5a28-446f-9cb1-0661412da1d6)


### Known Bugs & Resolutions
- **Issue**: Task priority tags not updating immediately in the UI.  
  - **Resolution**: Updated the AJAX call in `task_update` (commit `c70995a`) to refresh the DOM after save.

---

## Deployment

- **Platform**: Deployed on [Heroku: https://djangotaskmanager-4150dc63d3e8.herokuapp.com/ ]  
- **Deployment Steps**:
  1. Create an account on the chosen platform.
  2. Clone the repository and push to a new remote (if required).
  3. Set required environment variables (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL`, etc.).
  4. Run migrations and collect static files.
  5. Confirm build/deployment logs for success.

- **Live Demo**: [Deployed Link](#)  
  *[Click Here)](https://djangotaskmanager-4150dc63d3e8.herokuapp.com/)*

---

## Credits

### Code & Resources
- **[Quill.js](https://quilljs.com/)** for rich text editing.
- **[Bootstrap](https://getbootstrap.com/)** & **[FastBootstrap snippets](https://fastbootstrap.com/components/modal/)** for styling and modals.
- **[BBBootstrap Timeline snippet](https://bbbootstrap.com/snippets/user-business-timeline-32289439)** for timeline ideas.
- **[Bootstrap Studio Blog Components](https://bootstrapstudio.io/docs/blog-components.html)** for additional layout inspiration.

### Special Thanks
- Thanks to the Django community for excellent documentation and support.
- Previous Bootcamp student examples (e.g., [Erikas-Ramanauskas/Milestone-Project-4](https://github.com/Erikas-Ramanauskas/Milestone-Project-4)) for guidance on best practices.

---

## License
https://quilljs.com/docs/quickstart - We utilised Quill.js for our rich text editor within the Task Detail Page
https://www.figma.com/community/file/892825410260715717/simple-kanban-board - UI Inspiration
https://www.figma.com/community/file/1291667577858062539/kanban-board-task-management
https://www.figma.com/community/file/1209724056553648259/website-wireframes-ui-kit-vol-1 - for wireframes and UI

We utilised ChatGPT, Github Copilot, Here's an Example of AI-Usage to assist with my linting close to deadline.

![image](https://github.com/user-attachments/assets/c24aaf7c-6f7e-4b93-ab6e-b0bb49e5a6f9)

---

> **Note**: Please keep this README updated as you add new features, fix bugs, or reorganize the project structure. A thorough and up-to-date README is a key component of a successful final project submission!
