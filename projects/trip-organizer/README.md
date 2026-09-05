# California · Stanford Move-in Trip

[![Live Site](https://img.shields.io/badge/Live%20Site-Cloudflare%20Workers-F38020?logo=cloudflare&logoColor=white)](https://california-trip-2026.xiangdi-lin.workers.dev)
[![Frontend](https://img.shields.io/badge/Frontend-HTML%20%2F%20CSS%20%2F%20JavaScript-blue)](#)
[![Mobile First](https://img.shields.io/badge/Design-Mobile--First-2ea44f)](#)
[![Bilingual](https://img.shields.io/badge/UI-Chinese%20%2F%20English-purple)](#)
[![Offline Ready](https://img.shields.io/badge/Default%20Mode-Offline%20Ready-success)](#)

A bilingual, mobile-first travel dashboard built for a real California relocation and Stanford move-in journey.

The project organizes a multi-day itinerary involving international flights, rental cars, hotels, relocation logistics, university housing check-in, shopping, sightseeing, dining, and airport transportation into a single interactive interface designed for practical use during travel.

## Live Demo

**[View the deployed site](https://california-trip-2026.xiangdi-lin.workers.dev)**

![California Stanford Move-in Trip preview](assets/preview.png)

---

## Overview

This project was created to support a real relocation from China to Stanford University in September 2026.

The main travel route is:

**Hangzhou → Hong Kong → Los Angeles → San Diego → Bakersfield → Fremont → Stanford**

The trip combines several different types of planning:

- International air travel
- Airport arrival and rental-car pickup
- Long-distance driving through California
- Retrieving stored belongings in San Diego
- Overnight hotel stays
- Stanford graduate housing move-in
- Resident parking logistics
- Local shopping and move-in supplies
- Bay Area sightseeing
- Restaurant planning
- Final airport drop-off at SFO

Rather than keeping this information across reservation emails, screenshots, notes, map searches, and separate booking pages, I designed a single travel interface that consolidates the most useful information into one place.

The project is intentionally lightweight and practical. It is not intended to replicate a full travel-planning platform. Instead, it focuses on reducing friction during the trip by surfacing the right information at the right time.

---

## Design Goals

The project was developed around several practical constraints.

### 1. Mobile-first use

The site is primarily intended to be opened on a phone while traveling.

The interface therefore prioritizes:

- Fast scanning
- Large tap targets
- Compact information density
- Clear visual hierarchy
- Minimal navigation depth
- Responsive layouts
- Low loading overhead

### 2. Real-world scheduling constraints

The itinerary contains several fixed anchors, including:

- International flights
- Rental-car pickup and return
- Hotel check-in and checkout
- Stanford housing check-in
- Attraction reservations
- Airport departure

These fixed events are treated as hard scheduling constraints, with flexible activities planned around them.

### 3. Cross-time-zone reliability

The trip moves from China and Hong Kong to California.

All major timed events use explicit UTC offsets rather than relying only on browser-local time.

This allows the countdown and scheduling logic to remain correct when the site is opened:

- Before departure in China
- During the Hong Kong connection
- After arrival in California
- On devices configured to different time zones

### 4. Public privacy

The website is publicly accessible, so only information needed for planning and navigation is shown.

Sensitive data is intentionally excluded.

### 5. Offline resilience

The core site remains a single static HTML file with inline CSS, JavaScript, and SVG.

The default map experience is available without loading external mapping libraries.

Online features are loaded only when explicitly requested.

---

## Key Features

