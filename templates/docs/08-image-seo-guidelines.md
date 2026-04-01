# Image SEO Guidelines — [PROJECT_NAME]

## Purpose

Define image optimization standards for all [PROJECT_NAME] pages: alt text, file naming, compression, Open Graph/Twitter Cards, and image sitemap rules.

---

## 1. Alt Text Formula

### Standard Format

```
{Descriptive text of what the image shows} - {feature or context} | [PROJECT_NAME]
```

### Examples by Page Type

| Page Type | Image | Alt Text |
|-----------|-------|----------|
| Homepage | Hero showing digital profile | "Smart digital identity profile on mobile device - [PROJECT_NAME] platform overview \| [PROJECT_NAME]" |
| Hub | Business card mockup | "Digital business card with NFC sharing enabled - business identity \| [PROJECT_NAME]" |
| Use Case | Doctor using card | "Doctor sharing digital business card with patient via QR code \| [PROJECT_NAME]" |
| Comparison | Feature table screenshot | "[PROJECT_NAME] vs HiHello feature comparison table \| [PROJECT_NAME]" |
| Blog | Infographic | "How NFC business cards work - tap to share contact details infographic \| [PROJECT_NAME]" |
| Product | Physical card photo | "Metal NFC business card with custom design - [PROJECT_NAME] physical card \| [PROJECT_NAME]" |

### Rules

- Every image must have an alt attribute (never empty `alt=""` unless purely decorative)
- Include the page's primary keyword naturally when relevant (not forced)
- Describe what the image actually shows (accessibility first)
- Keep under 125 characters
- Don't start with "Image of" or "Photo of"
- For decorative images (dividers, backgrounds): use `alt=""`
- For icons: describe the function, not the appearance ("search icon" not "magnifying glass")

---

## 2. File Naming Convention

### Format

```
profiletap-{page-slug}-{description}.{ext}
```

### Examples

```
profiletap-business-identity-hero-digital-card.webp
profiletap-digital-business-card-doctors-qr-sharing.webp
profiletap-hihello-comparison-feature-table.webp
profiletap-blog-nfc-vs-qr-infographic.webp
profiletap-metal-nfc-card-product-photo.webp
```

### Rules

- All lowercase
- Hyphens only (no underscores, no spaces, no special characters)
- Include page slug for context
- Include descriptive keywords
- Keep filename under 80 characters
- Use consistent prefixing (`profiletap-`) for brand signals

---

## 3. Image Format and Compression

### Format Selection

| Use Case | Format | Why |
|----------|--------|-----|
| Photographs, hero images | WebP | Best compression-to-quality ratio |
| Screenshots, UI mockups | WebP or PNG | Sharp edges, text readability |
| Icons, logos | SVG | Scalable, tiny file size |
| Animated content | WebP (animated) or MP4 | Better than GIF |
| Fallback (older browsers) | JPEG / PNG | WebP with JPEG/PNG fallback via `<picture>` |

### Compression Targets

| Image Type | Max File Size | Max Dimensions |
|-----------|:---:|:---:|
| Hero/banner | 150 KB | 1920 x 1080 |
| In-content image | 100 KB | 1200 x 800 |
| Thumbnail | 30 KB | 400 x 300 |
| Icon | 5 KB | 64 x 64 |
| Product photo | 200 KB | 1200 x 1200 |

### Implementation

```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="{alt text}" width="1200" height="800" loading="lazy">
</picture>
```

### Rules

- Always set explicit `width` and `height` attributes (prevents CLS)
- Use `loading="lazy"` for below-fold images
- Use `loading="eager"` (or no attribute) for above-fold/hero images
- Preload hero image: `<link rel="preload" as="image" href="hero.webp">`
- Serve responsive sizes with `srcset` for different viewport widths

---

## 4. Open Graph Tags

### Standard Template (All Pages)

```html
<meta property="og:type" content="{type}">
<meta property="og:title" content="{page title}">
<meta property="og:description" content="{meta description}">
<meta property="og:url" content="{canonical URL}">
<meta property="og:image" content="{OG image URL}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{alt text}">
<meta property="og:site_name" content="[PROJECT_NAME]">
<meta property="og:locale" content="en_IN">
```

### Type by Page

| Page Type | og:type |
|-----------|---------|
| Homepage | website |
| Hub / Category / Use Case | website |
| Comparison | article |
| Blog | article |
| Product | product |

### OG Image Requirements

- **Dimensions:** 1200 x 630 pixels (1.91:1 ratio)
- **Format:** JPEG or PNG (not WebP — some platforms don't support it)
- **File size:** < 300 KB
- **Content:** Page title text overlaid on branded background
- **Template:** Consistent [PROJECT_NAME] branding (logo, colors, fonts)

### OG Image Naming

```
profiletap-og-{page-slug}.jpg
```

---

## 5. Twitter Card Tags

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@profiletap">
<meta name="twitter:title" content="{page title}">
<meta name="twitter:description" content="{meta description}">
<meta name="twitter:image" content="{OG image URL}">
<meta name="twitter:image:alt" content="{alt text}">
```

- Use `summary_large_image` for all pages (better visual presence)
- Can reuse the same OG image
- Test with Twitter Card Validator before launch

---

## 6. Image Sitemap

### When to Include

Include images in sitemap when:
- Product photos (future product catalog)
- Infographics that should appear in Google Images
- Unique illustrations or diagrams

### Format

```xml
<url>
  <loc>https://[SITE_URL]/digital-business-card-india</loc>
  <image:image>
    <image:loc>https://[SITE_URL]/images/profiletap-digital-business-card-india-hero.webp</image:loc>
    <image:title>Digital Business Card India - [PROJECT_NAME]</image:title>
    <image:caption>Create and share digital business cards with NFC and QR in India</image:caption>
  </image:image>
</url>
```

### Rules

- Include in main sitemap OR separate `/sitemap-images.xml`
- Only include meaningful images (not icons, backgrounds, decorative)
- Maximum 1,000 images per sitemap URL entry
- Update when images change

---

## 7. Image SEO Checklist (Per Page)

Before publishing any page:

- [ ] All images have descriptive alt text following the formula
- [ ] All images use the file naming convention
- [ ] All images are compressed (within size targets)
- [ ] WebP format used with JPEG/PNG fallback
- [ ] `width` and `height` attributes set on all `<img>` tags
- [ ] Above-fold images load eagerly, below-fold images lazy-load
- [ ] Hero image is preloaded
- [ ] OG image created (1200x630) with branded template
- [ ] Twitter Card tags present
- [ ] OG tags present and correct
- [ ] Test OG/Twitter preview with sharing debugger tools
