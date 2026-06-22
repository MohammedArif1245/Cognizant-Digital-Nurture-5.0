import { courses } from "./data.js";

// =========================
// ES6 Array Methods
// =========================

// Step 30
courses.forEach(({ name, credits }) => {
    console.log(name, credits);
});

// Step 31
const courseList = courses.map(
    course => `${course.code} - ${course.name} (${course.credits} credits)`
);

console.log(courseList);

// Step 32
const filterCourse = courses.filter(
    course => course.credits >= 4
);

console.log(filterCourse);
console.log(filterCourse.length);

// Step 33
const totalCredits = courses.reduce(
    (sum, course) => sum + course.credits,
    0
);

console.log(totalCredits);

// Step 34
courses.forEach(course =>
    console.log(`${course.code} - ${course.name}`)
);

// =========================
// DOM Elements
// =========================

const courseGrid = document.querySelector(".course-grid");
const searchInput = document.querySelector("#search-courses");
const sortButton = document.querySelector("#sort-btn");
const totalCreditsElement = document.querySelector("#total-credits");
const selectedCourse = document.querySelector("#selected-course");

// =========================
// Render Function
// =========================

function renderCourses(courseArray) {

    // Remove existing cards
    courseGrid.innerHTML = "";

    courseArray.forEach(course => {

        const article = document.createElement("article");

        article.className = "course-card";

        // Used for Event Delegation
        article.dataset.name = course.name;
        article.dataset.grade = course.grade;

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p>Course Code: ${course.code}</p>
            <span>Credits: ${course.credits}</span>
        `;

        courseGrid.appendChild(article);

    });

}

// Initial Render
renderCourses(courses);

// =========================
// Total Credits
// =========================

totalCreditsElement.textContent =
    `Total Credits: ${totalCredits}`;

// =========================
// Search Courses
// =========================

searchInput.addEventListener("input", () => {

    const searchValue = searchInput.value.toLowerCase();

    const filteredCourses = courses.filter(course =>
        course.name.toLowerCase().includes(searchValue)
    );

    renderCourses(filteredCourses);

});

// =========================
// Sort by Credits
// =========================

sortButton.addEventListener("click", () => {

    const sortedCourses = [...courses];

    sortedCourses.sort((a, b) => b.credits - a.credits);

    renderCourses(sortedCourses);

});

// =========================
// Event Delegation
// =========================

courseGrid.addEventListener("click", (event) => {

    const card = event.target.closest(".course-card");

    if (!card) return;

    selectedCourse.textContent =
        `Selected Course: ${card.dataset.name} | Grade: ${card.dataset.grade}`;

    // OR use this instead if your instructor wants an alert:
    // alert(`${card.dataset.name} - Grade: ${card.dataset.grade}`);

});