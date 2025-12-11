# Frontend (React + Vite) blueprint

This folder will host the Kenya Pool Leaderboard web app. Recommended setup:

- Initialize with `npm create vite@latest frontend -- --template react-ts` and move the resulting files here.
- Install libraries: `react-router-dom`, `@tanstack/react-query`, `axios`, `tailwindcss`, `daisyui` (optional), `zod` for schema validation.
- Configure an Axios instance that points to the Django API (e.g., `http://localhost:8000/api/`) and attaches auth tokens/CSRF.
- Provide top-level routes: `/dashboard`, `/leaderboards/:scope`, `/pools`, `/games`, `/reports`, `/admin`.
- Create reusable UI primitives (cards, tables, form inputs) that can be shared with the mobile app design language.

Directory suggestions:

```
src/
  api/        # Axios client, hooks
  components/ # UI building blocks
  features/   # Feature slices (leaderboards, games, pools)
  pages/      # Page-level components
  routing/    # Router setup
  styles/     # Tailwind config and global styles
```
