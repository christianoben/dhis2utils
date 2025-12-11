# Mobile (Expo/React Native) blueprint

Android-first client built with Expo and React Native:

- Initialize with `npx create-expo-app mobile --template` (TypeScript) and move the files here.
- Libraries: `@react-navigation/native`, `@react-navigation/native-stack`, `@react-navigation/bottom-tabs`, `@tanstack/react-query`, `axios`, `expo-location`, `expo-notifications` (optional), and `react-native-maps`.
- Screens: Dashboard, Leaderboards, Games (challenge/accept/result), Pools (for owners), Notifications, Profile.
- Use the same API surface as the web client; share request/response types via generated OpenAPI types when added.
- Ensure Africa/Nairobi timezone handling for game times and reports.
