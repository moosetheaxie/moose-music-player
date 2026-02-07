# Axie UI Spec (v1)

Based on `Axie_Infinity_Brand_Guideline.pdf` (Sep 2023).

## Brand tokens used

- Axie Orange: `#FFB300`
- Axie Black: `#0D0E12`
- Wood 300: `#3A1E10`
- Paper 100: `#FFF2DF`
- Blue 400: `#042055`
- Blue 300: `#0D51D3`
- Blue 200: `#0094FF`
- Blue 100: `#78B9FB`
- Accent (UI only): `#FF433E`, `#AFDB1B`, `#00F5F8`

## Visual direction

- Dark fantasy game-card look with high-contrast CTAs
- Use Orange for primary actions and highlights
- Use Blue gradient for interactive cards
- Keep copy left-aligned and readable
- Rounded cards, subtle shadows, clear game-like hierarchy

## Component mapping

- App shell: dark blue gradient background + glass cards
- Header: title, subtitle, online badge
- Search: prominent input with icon and active focus state
- Results: card rows with hover motion and action affordance
- Now playing: featured card with title/artist + pulse indicator
- Quick actions: chip buttons for frequent tracks
- Controls: circular transport controls
- Volume: styled track with orange thumb
- Backend config: hidden behind advanced toggle

## UX constraints

- Mobile-first layout
- Preserve existing backend contract (`/search`, `/play`, `/stop`, `/volume`, `/status`)
- Preserve backend URL override path for debugging
- Keep status feedback visible at all times
