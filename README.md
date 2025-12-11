# Kenya Pool Leaderboard System

A monorepo starter for the Kenya Pool Leaderboard platform featuring:

- **Backend:** Python + Django REST Framework API covering players, pools, games, leaderboards, recommendations, and notifications.
- **Web frontend (proposed):** React + Vite + React Query + Tailwind CSS for a responsive admin/owner/player experience.
- **Mobile (Android-first, proposed):** React Native (Expo) with React Query and native navigation for players and pool owners.

## Repository layout

- `backend/` – Django project (`kenya_pool`) and modular apps for accounts, locations, pools, games, leaderboards, recommendations, and notifications.
- `frontend/` – Placeholder for the React single-page app (SPA) with suggested tooling and folder structure.
- `mobile/` – Placeholder for the Expo/React Native app with suggested tooling and folder structure.
- `dhis2_data_pull.py` – Existing script left untouched.

## Getting started (backend)

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv backend/.venv
   source backend/.venv/bin/activate
   pip install -r backend/requirements.txt
   ```

2. Run migrations and create a superuser:

   ```bash
   python backend/manage.py migrate
   python backend/manage.py createsuperuser --phone_number +2547XXXXXXX
   ```

3. Start the development server:

   ```bash
   python backend/manage.py runserver
   ```

   APIs will be available under `/api/` (e.g., `/api/pools/`).

## Frontend approach

The frontend is expected to be a Vite-powered React SPA. Recommended stack:

- Vite + TypeScript for fast builds.
- React Query for data fetching and caching.
- React Router for navigation (dashboard, leaderboards, games, pools, reports).
- Tailwind CSS for rapid UI development.
- Axios client configured to the Django REST API with token/session support.

## Mobile approach (Android-first)

Use Expo + React Native + TypeScript:

- React Navigation for stacks/tabs (Dashboard, Leaderboards, Games, Notifications, Profile).
- React Query with an Axios client pointing to the API (same models as web).
- Expo Location & Maps for pool discovery; optional push notifications via Expo Notifications.
- Offline-first tweaks via React Query persistence if needed.

Each client should follow the API schema defined in the backend apps and reuse shared types generated from the OpenAPI schema when added.
