![strava](https://github.com/user-attachments/assets/aa4a0b43-e73e-4ef9-bb0e-608d7ae20e75)

# Strava-Utils

## Authentication

Example

```
export STRAVA_ACCESS_CODE=83ebeabdec09f6670863766f792ead24d61fe3f9
```

## Programs

### Dump All Activities

[dump\_activities.py](/dump_activities.py)

Dump the full list of activities. Max up to 20,000 activities before hitting
rate limits. Output to "activities.json" file.

### Plot Monthly Distance

[plot\_monthly\_distance.py](/plot_monthly_distance.py)

Line plot of monthly distance from activities in the previous year.

![monthly distance line plot](https://github.com/user-attachments/assets/7c0e4b0d-413f-4180-ac76-9b533169b52a)

### Plot Annual Distance

[plot\_annual\_distance.py](/plot_annual_distance.py)

Bar chart of annual distance from activities in the past 5 years.

![annual distance bar chart](https://github.com/user-attachments/assets/09128fb2-d53f-474c-8da9-2d2c23648867)

