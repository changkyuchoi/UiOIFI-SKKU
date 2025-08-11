from bs4 import BeautifulSoup
import csv

# Load your HTML content
with open('/Users/changkyuchoi/Documents/GitHub/UiOIFI-SKKU/bins/courses2025.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')
courses = []

for row in rows:
    button = row.find('button', class_='course-toggle')
    if button:
        course_code = button.text.strip()
        description = button.get('data-description', '').strip()
        tds = row.find_all('td')
        if len(tds) >= 8:
            # Ensure robust text extraction from all tags inside td
            def clean_text(td):
                return ' '.join(td.stripped_strings)

            course = {
                'course': course_code,
                'title': clean_text(tds[1]),
                'year': clean_text(tds[2]),
                'sem': clean_text(tds[3]),
                'campus': clean_text(tds[4]),
                'track': clean_text(tds[5]),
                'level': clean_text(tds[6]),
                'credits': clean_text(tds[7]),
                'desc': description
            }
            courses.append(course)

# Write to CSV with quotes around all fields to ensure robustness
with open('courses2025.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['course', 'title', 'year', 'sem', 'campus', 'track', 'level', 'credits', 'desc']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(courses)

print(f"{len(courses)} courses exported to CSV.")
