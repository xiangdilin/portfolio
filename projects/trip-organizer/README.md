# California · Stanford Move-in Trip

[![Live Site](https://img.shields.io/badge/Live%20Site-Cloudflare%20Workers-F38020?logo=cloudflare&logoColor=white)](https://california-trip-2026.xiangdi-lin.workers.dev)
[![HTML](https://img.shields.io/badge/Frontend-HTML%20%2F%20CSS%20%2F%20JavaScript-blue)](#)
[![Mobile First](https://img.shields.io/badge/Design-Mobile--First-2ea44f)](#)
[![Bilingual](https://img.shields.io/badge/UI-Chinese%20%2F%20English-purple)](#)
[![Offline Ready](https://img.shields.io/badge/Architecture-Single--File-success)](#)

A bilingual, mobile-first travel dashboard built for a real California relocation and Stanford move-in journey.

The project turns a multi-day itinerary — including international flights, rental cars, hotel stays, moving logistics, university housing check-in, and Bay Area day trips — into a compact, interactive, and publicly deployable web application.

## Live Demo

**[View the deployed site](https://california-trip-2026.xiangdi-lin.workers.dev)**

The site is hosted on Cloudflare Workers and automatically redeploys whenever the connected GitHub repository is updated.

---

## Overview

This project was created to support a real move from China to Stanford University in September 2026.

The travel route includes:

**Hangzhou → Hong Kong → Los Angeles → San Diego → Bakersfield → Fremont → Stanford**

The first half of the trip focuses on relocation logistics:

- International travel to California
- Immigration and rental-car pickup at LAX
- Retrieving stored belongings in San Diego
- Driving north through California
- Moving into Stanford graduate housing

The second half transitions into lighter family day trips around the Bay Area before the return flight.

Rather than keeping the plan in scattered reservation emails, screenshots, and notes, I designed a single travel interface that consolidates the most useful information into one place.

---

## Key Features

### Dynamic Next-Event Countdown

The homepage automatically identifies the next scheduled travel event and displays a live countdown in:

- Days
- Hours
- Minutes
- Seconds

All major timestamps are stored with explicit time-zone offsets, so countdowns remain correct even when the page is opened in different countries or device time zones.

---

### Time-Zone-Aware Scheduling

The itinerary spans multiple time zones:

- China Standard Time / Hong Kong Time: `UTC+8`
- Pacific Daylight Time: `UTC-7`

Flight and itinerary events are represented using absolute timestamps rather than relying on the user's browser time zone.

This prevents incorrect countdowns during international travel.

---

### Bilingual Interface

The page includes a built-in language switch between:

- Chinese
- English

The Chinese interface intentionally keeps a natural Chinese-English mixed travel style, while the English mode renders the interface fully in English.

The selected language is saved locally in the browser.

---

### Interactive Route Planning

Each day includes:

- A simplified route visualization
- Clickable location links
- Google Maps integration
- One-click multi-stop driving navigation

The overall itinerary also includes a custom inline SVG route map showing the progression from Southern California to the Bay Area.

---

### Mobile-First UI

The site is designed primarily for use during travel on a phone.

Design priorities include:

- Large tap targets
- Compact information cards
- Responsive daily timelines
- Minimal loading overhead
- Clear visual distinction between confirmed and tentative items

---

### Automatic Light / Dark Theme

The interface automatically switches color themes based on the local device time.

This makes the page easier to use both during daytime travel and late-night airport or hotel situations.

---

### Privacy-Aware Public Design

Because the deployed website is publicly accessible, sensitive reservation and identity information is deliberately excluded.

The public page does **not** contain:

- Passport numbers
- Government ID numbers
- Visa details
- EVUS or SEVIS identifiers
- Airline PNRs
- Electronic ticket numbers
- Hotel booking IDs
- Credit card information
- Storage unit numbers
- Access codes
- Exact apartment numbers

Only information useful for travel planning and navigation is included.

---

## Stanford Move-in Logistics

The itinerary includes dedicated move-in planning for Stanford graduate housing, including:

- EVGR check-in timing
- Housing Service Center location
- Move-in parking constraints
- Parking permit reminders
- Construction-related access considerations
- Post-move resident parking requirements

The site also distinguishes between temporary moving logistics and longer-term resident parking.

---

## Tech Stack

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript
- Inline SVG

### Deployment

- GitHub
- Cloudflare Workers
- Git-based automatic deployment

### External Integrations

- Google Maps navigation links

No JavaScript framework, CSS framework, package manager, or build tool is required.

---

## Architecture

The project intentionally uses a minimal single-file architecture.

```text
.
├── index.html
├── README.md
└── assets/
    └── preview.png
