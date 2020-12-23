# Site Name Creator - Namer

## Primary Function
Provides a class and a function to create a name based on information provided by assigned sources.

## What makes up a site name

1. Brand Code - IE: BB1 (max 3)
2. Country Code - IE: AUS (max3, use global country code - ISO3166)
3. Club/Site Name - IE: THISISSITE1 (max12)

- Total character length of name is max 18 characters including the '-' symbols.

### Examples

```text
BB1-AUS-THISISSITE1
```

```text
BB2-AUS-SITE1
```

```text
BB3-THA-RANDOMSITE1
```

## Summary of functional tasks

1. Need to be able to obtain a list of brands that are part of the brands.csv file
2. End user can select which brand
3. Naming of site is built from brand
4. Need a shortened naming convention defined and in a config file


## How will it create a sitename?

1. All brands will have a corresponding abbrieviated name ie Brand1 = BB1. This will be stored in the brands.csv file.
2. All brands will have specific regions they are located in, some brands will be in multiple regions, when this is the case they will be taken to another menu to select which specific region they are deploying the new network site to.
3. When brand and region is selected, the user will now need to input the site name, with a maximum of 12 characters allowed.

## Current list of sources

1. Brand Code: CSV File - "config/site_data/brands.csv" [BrandCode]
2. Country Code: CSV File - "config/site_data/brands.csv" [CountryCode]
3. Club/Site Name: User inputted

# Site Name Creator - Brander

## Primary Function
T