# Local SEO Strategy and Execution

## Skill Metadata
- **Command**: `/local-seo`
- **Purpose**: Plan and execute local SEO strategy for any business with a physical presence or service area
- **Output**: Local SEO implementation plan with checklists, templates, and prioritized action items

---

## 1. Google Business Profile Optimization Checklist

### Profile Completeness (Complete Every Field)
- [ ] **Business name**: Exact legal business name — no keyword stuffing
- [ ] **Primary category**: Most specific category that describes your core business
- [ ] **Secondary categories**: Add all relevant secondary categories (up to 9 additional)
- [ ] **Address**: Full street address for storefront businesses; hide address for service-area businesses
- [ ] **Service area**: Define service regions for service-area businesses (up to 20 areas)
- [ ] **Phone number**: Local phone number preferred over toll-free (signals local relevance)
- [ ] **Website URL**: Link to the most relevant local landing page, not necessarily the homepage
- [ ] **Business hours**: Accurate regular hours, including special hours for holidays
- [ ] **Business description**: 750 characters max — include primary services, location, and differentiators. No promotional language or URLs.
- [ ] **Opening date**: Set the correct opening date (helps with "established" queries)
- [ ] **Attributes**: Complete all available attributes (wheelchair accessible, Wi-Fi, outdoor seating, etc.)

### Photos and Media
- [ ] **Logo**: High-resolution logo (250x250 minimum)
- [ ] **Cover photo**: Representative image of the business (1080x608 minimum)
- [ ] **Interior photos**: 3-5 photos showing the inside of the business
- [ ] **Exterior photos**: 2-3 photos showing the building and signage
- [ ] **Team photos**: 2-3 photos of staff or team members
- [ ] **Product/service photos**: 5-10 photos of key products or services
- [ ] **Upload frequency**: Add new photos at least monthly to signal activity
- [ ] **Geotagging**: Ensure photo EXIF data includes GPS coordinates of the business location

### Google Business Profile Posts
- **Frequency**: Post at least once per week
- **Post types**: Offers, events, updates, product highlights
- **Content guidelines**: 150-300 words, include a CTA button, add a relevant image
- **Expiration**: "What's New" posts expire after 7 days; Event posts expire after the event date
- **Keywords**: Naturally include local keywords in post text

### Products and Services
- [ ] Add all products with descriptions, prices, and photos
- [ ] Add all services organized by service category
- [ ] Include relevant keywords naturally in product/service descriptions
- [ ] Link each product/service to the relevant page on your website

### Q&A Management
- [ ] Seed 10-20 common questions and answer them yourself (Google allows this)
- [ ] Monitor for new questions weekly and respond within 24 hours
- [ ] Upvote the most helpful Q&A entries
- [ ] Report spam or inappropriate questions

---

## 2. Local Citation Building Strategy

### NAP Consistency Rules
NAP = Name, Address, Phone Number. Consistency across all citations is critical.

1. **Exact match**: Business name must be identical everywhere — same spelling, same abbreviations (or lack thereof), same punctuation
2. **Address format**: Choose one format and use it everywhere (e.g., "Street" vs "St." — pick one)
3. **Phone number**: Use the same primary phone number on all citations. Format consistently (e.g., (555) 123-4567 everywhere)
4. **Suite/unit numbers**: Include or exclude consistently
5. **Website URL**: Use the same URL format (with or without www, with or without trailing slash)

### NAP Audit Process
1. Search your business name + city on Google to find existing citations
2. Use a citation audit tool (BrightLocal, Moz Local, or Whitespark) to scan for inconsistencies
3. Create a master NAP record as the single source of truth
4. Correct all inconsistent citations starting with the highest-authority sources
5. Re-audit quarterly to catch new inconsistencies

### Citation Building Priority Order
Build citations in this order for maximum impact:

**Tier 1 — Essential (Do First)**
- Google Business Profile
- Apple Maps (Apple Business Connect)
- Bing Places for Business
- Facebook Business Page
- Yelp

**Tier 2 — Major Aggregators**
- Data Axle (Infogroup)
- Neustar/Localeze
- Foursquare
- Factual

**Tier 3 — General Directories**
- Better Business Bureau (BBB)
- Yellow Pages (YP.com)
- Angi (formerly Angie's List)
- Thumbtack
- MapQuest
- Superpages
- CitySearch
- Local.com
- Manta
- DexKnows

**Tier 4 — Industry-Specific Directories**
Varies by industry. Examples:
- Healthcare: Healthgrades, Vitals, Zocdoc, WebMD
- Legal: Avvo, FindLaw, Justia, Lawyers.com
- Real Estate: Zillow, Realtor.com, Trulia
- Restaurants: TripAdvisor, OpenTable, Zomato
- Home Services: HomeAdvisor, Houzz, Porch
- Hospitality: TripAdvisor, Booking.com, Hotels.com

**Tier 5 — Local/Regional Directories**
- Local Chamber of Commerce
- City/county business directories
- Regional industry associations
- Local newspaper business listings
- Community websites and forums

---

## 3. Local Schema Markup Templates

### LocalBusiness Schema (JSON-LD)
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "description": "Brief business description with local keywords",
  "url": "https://www.example.com",
  "telephone": "+1-555-123-4567",
  "email": "contact@example.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main Street, Suite 100",
    "addressLocality": "City Name",
    "addressRegion": "ST",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "40.7128",
    "longitude": "-74.0060"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "17:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "10:00",
      "closes": "14:00"
    }
  ],
  "image": "https://www.example.com/images/storefront.jpg",
  "logo": "https://www.example.com/images/logo.png",
  "priceRange": "$$",
  "sameAs": [
    "https://www.facebook.com/businessname",
    "https://www.instagram.com/businessname",
    "https://www.linkedin.com/company/businessname"
  ],
  "areaServed": {
    "@type": "City",
    "name": "City Name"
  }
}
```

### Organization with Multiple Locations
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Parent Organization Name",
  "url": "https://www.example.com",
  "logo": "https://www.example.com/images/logo.png",
  "subOrganization": [
    {
      "@type": "LocalBusiness",
      "name": "Business Name - Location 1",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "123 Main St",
        "addressLocality": "City A",
        "addressRegion": "ST",
        "postalCode": "11111"
      },
      "telephone": "+1-555-111-1111",
      "url": "https://www.example.com/locations/city-a"
    },
    {
      "@type": "LocalBusiness",
      "name": "Business Name - Location 2",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "456 Oak Ave",
        "addressLocality": "City B",
        "addressRegion": "ST",
        "postalCode": "22222"
      },
      "telephone": "+1-555-222-2222",
      "url": "https://www.example.com/locations/city-b"
    }
  ]
}
```

### Use More Specific @type When Applicable
Replace `LocalBusiness` with the most specific subtype:
- `Restaurant`, `BarOrPub`, `CafeOrCoffeeShop`
- `Dentist`, `Physician`, `MedicalClinic`
- `LegalService`, `Attorney`
- `RealEstateAgent`
- `AutoRepair`, `AutoDealer`
- `BeautySalon`, `HairSalon`
- `FinancialService`, `InsuranceAgency`

---

## 4. Review Generation Strategy

### Timing
- Ask for a review 1-3 days after a positive service experience
- For product businesses: after delivery confirmation + 3-5 days of use
- For service businesses: within 24-48 hours of service completion
- Never ask during or immediately after a negative experience

### Channels (Prioritized)
1. **Direct link via email/SMS**: Send a short message with a direct Google review link
2. **In-person ask**: Train staff to ask satisfied customers verbally, then follow up with a link
3. **Post-purchase automation**: Trigger an automated email/SMS sequence after transactions
4. **QR code**: Place QR codes linking to your review page at checkout, on receipts, or on table cards
5. **Website widget**: Add a "Leave a Review" CTA on your thank-you or post-purchase page

### Google Review Link Format
```
https://search.google.com/local/writereview?placeid=YOUR_PLACE_ID
```
Find your Place ID at: https://developers.google.com/maps/documentation/places/web-service/place-id

### Review Response Templates

**Positive Review Response:**
```
Thank you [Name]! We're glad [specific detail from their review].
We appreciate you taking the time to share your experience, and we
look forward to serving you again.
```

**Negative Review Response:**
```
[Name], thank you for sharing your feedback. We're sorry to hear
about [specific issue mentioned]. This doesn't reflect our standard,
and we'd like to make it right. Please contact us at [email/phone]
so we can address this directly.
```

### Review Response Rules
1. Respond to every review — positive and negative — within 48 hours
2. Personalize each response (reference specific details from the review)
3. Never argue, be defensive, or disclose private information in public responses
4. For negative reviews, take the conversation offline (provide contact info)
5. Thank the reviewer regardless of sentiment
6. Include a natural keyword mention when it fits (e.g., "We love providing [service] to [city] residents")

### Review Velocity Target
- New businesses: Aim for 5-10 reviews in the first month
- Established businesses: Aim for 2-5 new reviews per month consistently
- Never buy reviews, incentivize reviews with discounts, or gate reviews (ask only happy customers). These violate Google's policies.

---

## 5. Local Content Creation Guidelines

### City/Region Landing Page Methodology

**Minimum Unique Content Requirements:**
Each city/region page must have at least 60% unique content. Avoid cookie-cutter pages that swap only the city name.

**Page Structure:**
1. **H1**: "[Service/Product] in [City/Region]" (unique to each page)
2. **Introduction** (150-200 words): Describe your services specific to this area, mention local landmarks, neighborhoods, or characteristics
3. **Services section** (200-400 words): Detail services offered in this area with any location-specific variations
4. **Local expertise section** (150-250 words): Explain why you are qualified to serve this area — years serving the community, local knowledge, local team members
5. **Area information** (100-200 words): Relevant local details — neighborhoods served, nearby areas, local regulations or considerations
6. **Customer testimonials**: Embed 2-3 reviews from customers in that specific area
7. **Local contact information**: Address, phone, hours specific to this location
8. **Embedded Google Map**: Map showing your location or service area
9. **Local schema markup**: LocalBusiness JSON-LD specific to this location

**Avoiding Thin Content on City Pages:**
- Never use find-and-replace to swap city names across template pages
- Include genuinely unique information about each location (demographics, local challenges, community involvement)
- Add unique images from each location (storefront, team, local landmarks)
- Include location-specific case studies or testimonials
- Reference local events, organizations, or partnerships

### Local News and Community Content
- Cover local events your business participates in
- Write about local industry trends specific to your area
- Create guides: "Best [related businesses] in [City]" (link to complementary local businesses)
- Publish seasonal content tied to local weather, events, or traditions
- Interview local figures, customers, or community leaders

---

## 6. Local Link Building Tactics

### High-Value Local Link Sources

**Tier 1 — Institutional Links**
- [ ] Local Chamber of Commerce membership (usually includes a directory listing with dofollow link)
- [ ] Better Business Bureau accreditation
- [ ] Local government business directories
- [ ] Industry association memberships (local chapters)

**Tier 2 — Community Involvement**
- [ ] Sponsor local sports teams, school events, or community programs
- [ ] Participate in local charity events (links from charity websites)
- [ ] Host or sponsor local meetups (links from Meetup.com and event pages)
- [ ] Offer scholarships to local schools (links from .edu sites)
- [ ] Partner with local nonprofits (links from .org sites)

**Tier 3 — Content-Based Links**
- [ ] Contribute expert quotes to local news publications
- [ ] Write guest articles for local blogs or community websites
- [ ] Create a local resource guide that other businesses want to link to
- [ ] Develop local research or data (surveys, market reports) that journalists cite
- [ ] Produce local event calendars that community sites reference

**Tier 4 — Business Relationships**
- [ ] Exchange links with complementary (non-competing) local businesses
- [ ] Get listed on supplier or vendor partner pages
- [ ] Join local business networks or co-working spaces that maintain member directories
- [ ] Get featured in "businesses we recommend" lists from partners

### Link Building Outreach Template
```
Subject: [Community/partnership opportunity] in [City]

Hi [Name],

I'm [Your Name] from [Business Name] in [City]. I noticed
[specific reference to their organization/content/event].

[Specific value proposition — what you are offering: sponsorship,
content contribution, collaboration, resource they might want to
link to].

Would you be open to [specific ask]?

Best regards,
[Your Name]
```

---

## 7. Google Maps Optimization

### Ranking Factors for Google Maps (Local Pack)
1. **Relevance**: How well your profile matches the search query (categories, services, description)
2. **Distance**: Physical proximity of your business to the searcher
3. **Prominence**: Overall online reputation (reviews, citations, backlinks, brand mentions)

### Maps-Specific Optimization Actions
- [ ] Verify your business location through Google's verification process
- [ ] Pin your location precisely on the map (drag the pin to the exact spot)
- [ ] Add accurate latitude/longitude coordinates
- [ ] Ensure your address matches Google Maps' geocoding exactly
- [ ] Encourage check-ins and photo uploads from customers
- [ ] Embed Google Maps on your website's contact page and location pages
- [ ] Use the same address format on your website as on Google Maps
- [ ] Create and maintain Google Maps lists relevant to your business area

---

## 8. Multi-Location Strategy

### URL Structure
```
example.com/locations/                    (Location index page)
example.com/locations/city-name/          (City landing page)
example.com/locations/city-name/services/ (Optional: city-specific services)
```

### Per-Location Requirements
Each location must have:
- Its own Google Business Profile (separate GBP for each physical location)
- Its own dedicated landing page on the website
- Unique NAP information
- Location-specific schema markup
- Location-specific content (not duplicated across locations)
- Its own set of citations on major directories
- Its own review generation strategy

### Multi-Location Internal Linking
- Location index page links to all individual location pages
- Each location page links back to the location index
- Location pages do NOT link laterally to other location pages (prevents dilution)
- Service pages link to the most relevant location page when appropriate

### Avoiding Common Multi-Location Mistakes
1. Do not create location pages for areas where you have no physical presence (this violates Google's guidelines)
2. Do not use a single GBP with multiple addresses
3. Do not create dozens of thin city pages just to target more keywords
4. Do not use PO boxes or virtual offices as GBP addresses unless you genuinely operate from there
5. Each GBP should use a unique phone number (call tracking numbers are acceptable if consistent)

---

## 9. Local Keyword Research Methodology

### Keyword Pattern Templates
```
[service] + [city]                    → "plumber in Austin"
[service] + near me                   → "plumber near me"
[service] + [neighborhood]            → "plumber downtown Austin"
[service] + [zip code]                → "plumber 78701"
best + [service] + [city]             → "best plumber in Austin"
[service] + [city] + reviews          → "plumber Austin reviews"
[service] + [city] + cost/price       → "plumber Austin cost"
affordable + [service] + [city]       → "affordable plumber Austin"
emergency + [service] + [city]        → "emergency plumber Austin"
[service] + [city] + [qualifier]      → "licensed plumber Austin"
```

### Research Process
1. List all your services and products
2. List all target cities, neighborhoods, and regions
3. Create a matrix combining services with locations using the patterns above
4. Check search volume for each combination using Google Keyword Planner, Ubersuggest, or similar
5. Identify which combinations have meaningful volume (even 10-20/month matters for local)
6. Check Google Suggest and PAA for additional local query variations
7. Group keywords by landing page (one page per service-location combination)
8. Prioritize based on search volume, competition, and business value

### Local Intent Signals
A keyword has local intent when:
- It includes a city, neighborhood, zip code, or "near me"
- Google shows a Local Pack (map + 3 listings) in the SERP
- Google shows localized organic results (local businesses ranking)
- The service inherently requires physical presence (plumber, dentist, restaurant)

---

## 10. Output Format: Local SEO Implementation Plan

```
=== LOCAL SEO IMPLEMENTATION PLAN ===

Business Name: [Name]
Business Type: [Type / Industry]
Number of Locations: [Count]
Target Service Area: [Cities/Regions]
Plan Date: [Date]
Review Date: [Quarterly review date]

--- PHASE 1: FOUNDATION (Weeks 1-2) ---

Google Business Profile:
- [ ] Claim/verify all GBP listings
- [ ] Complete every profile field (see Section 1 checklist)
- [ ] Upload initial photo set (15+ photos per location)
- [ ] Add all products and services
- [ ] Seed Q&A with 10+ common questions
- [ ] Set up GBP posting calendar (weekly)

Website:
- [ ] Add LocalBusiness schema to all location pages
- [ ] Create/optimize location landing pages (see Section 5)
- [ ] Embed Google Maps on contact/location pages
- [ ] Ensure NAP is consistent across all website pages
- [ ] Add click-to-call functionality on mobile

--- PHASE 2: CITATIONS (Weeks 3-6) ---

- [ ] Audit existing citations for NAP consistency
- [ ] Correct all inconsistent citations
- [ ] Build Tier 1 citations (Google, Apple, Bing, Facebook, Yelp)
- [ ] Build Tier 2 citations (data aggregators)
- [ ] Build Tier 3 citations (general directories)
- [ ] Build Tier 4 citations (industry-specific directories)
- [ ] Build Tier 5 citations (local directories)
- Total target citations: [Number — typically 40-80 for most businesses]

--- PHASE 3: REVIEWS (Ongoing from Week 3) ---

- [ ] Create review generation process (see Section 4)
- [ ] Set up review monitoring alerts
- [ ] Create review response templates
- [ ] Train staff on review asking process
- [ ] Generate review link and distribute to team
- Monthly review target: [Number]

--- PHASE 4: LOCAL CONTENT (Weeks 5-12) ---

- [ ] Create/optimize city landing pages for each target area
- [ ] Publish [Number] local blog posts per month
- [ ] Develop local resource guides
- [ ] Add customer testimonials organized by location
- Local keyword targets: [List primary local keywords]

--- PHASE 5: LOCAL LINK BUILDING (Ongoing from Week 6) ---

- [ ] Join Chamber of Commerce
- [ ] Identify 5-10 local sponsorship opportunities
- [ ] Plan 2-3 community involvement activities per quarter
- [ ] Begin local PR / media outreach
- [ ] Develop local partnership link exchanges
- Monthly link building target: [Number of new local links]

--- TRACKING AND METRICS ---

Primary KPIs:
- Google Maps ranking for [top 5 local keywords]
- Local Pack appearances (number of keywords showing in 3-pack)
- GBP impressions and actions (calls, directions, website clicks)
- Review count and average rating
- Local organic traffic (GA4, filtered by target geo)
- Citation accuracy score (audit quarterly)

Reporting Cadence:
- Weekly: GBP insights, review monitoring
- Monthly: Rankings, traffic, citation audit, link building progress
- Quarterly: Full local SEO audit, strategy review, plan update
```

### Final Checklist Before Launch
- [ ] NAP is 100% consistent across website, GBP, and all citations
- [ ] Schema markup validates without errors (test at schema.org validator)
- [ ] All GBP fields are complete
- [ ] Location pages have 60%+ unique content each
- [ ] Review generation process is documented and staff are trained
- [ ] Local keyword targets are mapped to specific pages
- [ ] Tracking is set up (rank tracker, GBP insights, GA4 with local filters)
- [ ] Quarterly review date is scheduled
