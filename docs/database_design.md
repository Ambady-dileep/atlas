User
 │
 └── Technology
         │
         └── Topic
                 │
                 └── LearningLog

User
├── id
├── email
├── username
└── created_at

Technology
├── id
├── name
├── description
├── user_id
├── created_at
└── updated_at

Topic
├── id
├── title
├── status
├── technology_id
├── created_at
└── updated_at

Topic Status
├── NOT_STARTED
├── IN_PROGRESS
└── COMPLETED

LearningLog
├── id
├── note
├── duration_minutes
├── topic_id
├── created_at
└── updated_atfeat: initialize Atlas backend architecture and learning domain models

* Set up Django project structure with apps package architecture
* Configure environment variables using python-decouple
* Add .env and .env.example configuration support
* Create accounts app for future authentication features
* Create learning app for core learning-tracking functionality
* Configure Django app imports and project settings
* Add Django REST Framework dependency and configuration

Documentation:

* Add project documentation structure
* Create project_overview.md
* Create requirements.md
* Create roadmap.md
* Create database_design.md
* Create api_design.md
* Create architecture.md

Database Design:

* Design User → Technology → Topic → LearningLog hierarchy
* Define topic status workflow (Not Started, In Progress, Completed)
* Plan REST API endpoints for authentication and learning resources

Models:

* Create Technology model

  * name
  * description
  * user relationship
  * timestamps

* Create Topic model

  * title
  * status choices
  * technology relationship
  * timestamps

* Create LearningLog model

  * note
  * duration_minutes
  * topic relationship
  * timestamps

Relationships:

* User -> Technologies (One-to-Many)
* Technology -> Topics (One-to-Many)
* Topic -> LearningLogs (One-to-Many)

Database:

* Generate initial migrations
* Apply database schema successfully

This commit establishes the foundation of Atlas and completes Phase 1 backend domain modeling.



