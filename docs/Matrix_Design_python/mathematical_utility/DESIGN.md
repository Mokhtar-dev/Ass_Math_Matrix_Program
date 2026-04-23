---
name: Mathematical Utility
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#909097'
  outline-variant: '#45464d'
  surface-tint: '#bec6e0'
  primary: '#bec6e0'
  on-primary: '#283044'
  primary-container: '#0f172a'
  on-primary-container: '#798098'
  inverse-primary: '#565e74'
  secondary: '#b7c8e1'
  on-secondary: '#213145'
  secondary-container: '#3a4a5f'
  on-secondary-container: '#a9bad3'
  tertiary: '#2fd9f4'
  on-tertiary: '#00363e'
  tertiary-container: '#001b20'
  on-tertiary-container: '#008ea1'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#a2eeff'
  tertiary-fixed-dim: '#2fd9f4'
  on-tertiary-fixed: '#001f25'
  on-tertiary-fixed-variant: '#004e5a'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1280px
---

## Brand & Style

The design system is engineered for precision, efficiency, and clarity. It targets a professional audience that values technical accuracy over decorative flourishes. The aesthetic sits at the intersection of **Minimalism** and **Swiss International Style**, utilizing a rigid structural framework to organize complex data sets.

The UI should evoke a sense of "computational calm"—providing a high-density information environment that remains accessible through disciplined hierarchy. Visual noise is treated as a technical debt; every line, gap, and color choice must serve a functional purpose in the data-entry or analysis workflow.

## Colors

The color palette of this design system is rooted in deep, cinematic blues and professional slates to reduce eye strain during prolonged technical sessions. 

- **Primary Canvas:** A deep navy background provides a stable foundation for high-contrast data.
- **Accents:** A sharp Cyan is used exclusively for interactive elements, focus states, and primary actions. It acts as a beacon within the darker interface.
- **Data Layers:** Slate grays define the UI scaffolding, borders, and secondary text, creating a clear distinction between the container and the content.
- **Functional Colors:** Use a strictly calibrated green for success/positive trends and a high-chroma red for errors or critical thresholds, ensuring they are distinct from the primary cyan accent.

## Typography

Typography is the primary tool for communicating the "mathematical" nature of the design system. 

1. **Headlines & Labels:** **Space Grotesk** is used for its geometric, technical character. Its distinct letterforms provide a futuristic, precise feel.
2. **Body Text:** **Inter** is utilized for long-form reading and interface descriptions due to its exceptional legibility at small sizes.
3. **Data Representation:** For numerical values, coordinates, and input fields, the "mono-data" style should be prioritized. Tabular numerals must be used to ensure columns of figures align perfectly, facilitating quick comparison and scanning.
4. **Hierarchy:** Use uppercase labels with increased letter spacing for section headers to evoke a blueprint or technical schematic feel.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** approach based on a 4px baseline unit. 

- **Grid:** Use a 12-column grid for desktop views, collapsing to 4 columns on mobile.
- **Rhythm:** Spacing between elements should always be a multiple of 4 (4, 8, 12, 16, 24, 32, 48, 64).
- **Data Density:** The design system prioritizes vertical efficiency. Compact padding (8px or 12px) is preferred for lists and data tables to maximize the amount of visible information without sacrificing touch targets.
- **Readability:** Maintain a maximum line length of 60-70 characters for descriptive text, while allowing data tables to span the full width of the container for maximum horizontal context.

## Elevation & Depth

To maintain a technical, "flat" aesthetic, this design system avoids heavy drop shadows and traditional skeuomorphism. Depth is instead conveyed through **Tonal Layers** and **Low-Contrast Outlines**.

- **Surface Levels:** The base background is the darkest shade. Each elevated level (cards, modals, popovers) uses a slightly lighter shade of slate or navy to indicate its "height."
- **Borders as Dividers:** Use 1px solid borders in a low-opacity slate (`#64748B` at 20-30%) to define containers. This creates a crisp, architectural look.
- **Focus States:** High-elevation elements may utilize a very subtle outer glow in the accent Cyan color to indicate focus or active state, rather than a shadow.

## Shapes

The shape language of the design system is strictly **Sharp**. 

- **Zero Radius:** All buttons, input fields, cards, and containers feature 90-degree corners. This reinforces the mathematical, "undecorated" nature of a utility tool.
- **Consistency:** If a border is used, it must be a consistent 1px stroke. 
- **Icons:** Use thin-stroke, geometric icons with sharp terminals. Avoid rounded caps or bubbles; the iconography should feel like technical line drawings.

## Components

- **Buttons:** Sharp-edged boxes with high-contrast Cyan backgrounds for primary actions. Text is bold and all-caps. Secondary buttons use a transparent background with a 1px Cyan border.
- **Input Fields:** Bottom-border only or full-outline with zero radius. Labels should be small and positioned above the field. Use a distinct background color on focus to highlight the active entry point.
- **Data Tables:** Use subtle horizontal rules only; avoid vertical dividers unless comparing distinct datasets. Header rows should use the "label-caps" typography style with a slight slate background.
- **Chips/Status Indicators:** Rectangular blocks with a subtle background tint and high-contrast text. No rounded corners.
- **Progress Indicators:** Linear, thin bars using the Cyan accent. Avoid circular loaders; use incremental, "stepped" progress bars to emphasize the mathematical progression of tasks.
- **Charts:** Use the Cyan and Lime Green accents for data lines. Grid lines within charts should be visible but faint, set to the same 4px rhythm as the rest of the UI.