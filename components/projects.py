import streamlit as st


projects = [
    {
        "number": "01",
        "title": "Social Media Addiction Analysis",
        "category": "DATA SCIENCE",
        "description": (
            "Exploratory data analysis and statistical investigation "
            "of social media usage patterns."
        ),
        "technologies": [
            "Python",
            "Pandas",
            "NumPy",
            "Matplotlib",
            "Seaborn",
            "Linear Regression",
            "Hypothesis Testing"
        ],
        "github": "https://github.com/karank002/Social_media_addiction"
    },

    {
        "number": "02",
        "title": "Student Record Management System",
        "category": "DSA",
        "description": (
            "A student record management system built using "
            "data structures and algorithms."
        ),
        "technologies": [
            "C++",
            "Data Structures",
            "Algorithms"
        ],
        "github": "https://github.com/karank002/student-record-management-system"
    },

    {
        "number": "03",
        "title": "Advanced Disk Scheduling Simulator",
        "category": "SYSTEMS",
        "description": (
            "Simulator implementing multiple disk scheduling "
            "algorithms and calculating performance metrics."
        ),
        "technologies": [
            "C++",
            "FCFS",
            "SSTF",
            "SCAN",
            "C-SCAN"
        ],
        "github": "https://github.com/karank002/Disk-Schdeuling-Simulator-"
    },

    {
        "number": "04",
        "title": "Cassandra Messaging Backend",
        "category": "BACKEND",
        "description": (
            "Backend for real-time message storage and delivery "
            "using FastAPI and Cassandra."
        ),
        "technologies": [
            "Python",
            "FastAPI",
            "Cassandra",
            "REST API"
        ],
        "github": "https://github.com/karank002/cassandra-messaging-backend"
    },

    {
        "number": "05",
        "title": "Laser-Based Security System",
        "category": "HARDWARE",
        "description": (
            "Arduino-based security system that detects laser "
            "interruption and sends alerts."
        ),
        "technologies": [
            "Arduino",
            "LDR",
            "GSM",
            "Embedded Systems"
        ],
        "github": "#"
    }
]


def projects_section():

    st.markdown(
        "<h2>"
        "SELECTED <span class='accent'>WORK</span>"
        "</h2>",
        unsafe_allow_html=True
    )

    st.write(
        "A collection of projects I've built while exploring "
        "Data Science, systems and software development."
    )

    categories = [
        "ALL",
        "DATA SCIENCE",
        "DSA",
        "SYSTEMS",
        "BACKEND",
        "HARDWARE"
    ]

    selected = st.radio(
        "FILTER PROJECTS",
        categories,
        horizontal=True
    )

    if selected == "ALL":
        filtered_projects = projects
    else:
        filtered_projects = [
            project
            for project in projects
            if project["category"] == selected
        ]

    for project in filtered_projects:

        tech = " · ".join(project["technologies"])

        st.markdown(
            "<div class='portfolio-card'>"
            
            "<div style='font-size:14px;'>"
            + str(project["number"])
            + " · "
            + project["category"]
            + "</div>"

            "<h2>"
            + project["title"]
            + "</h2>"

            "<p>"
            + project["description"]
            + "</p>"

            "<p class='accent'>"
            + tech
            + "</p>"

            "</div>",
            
            unsafe_allow_html=True
        )

        if project["github"] != "#":
            st.link_button(
                "VIEW ON GITHUB →",
                project["github"]
            )


# def projects_section():

#     st.markdown(
#         """
#         <h2>
#             SELECTED <span class="accent">WORK</span>
#         </h2>
#         """,
#         unsafe_allow_html=True
#     )

#     st.write(
#         "A collection of projects I've built while exploring "
#         "Data Science, systems and software development."
#     )

#     categories = [
#         "ALL",
#         "DATA SCIENCE",
#         "DSA",
#         "SYSTEMS",
#         "BACKEND",
#         "HARDWARE"
#     ]

#     selected = st.radio(
#         "FILTER PROJECTS",
#         categories,
#         horizontal=True
#     )

#     if selected == "ALL":
#         filtered_projects = projects
#     else:
#         filtered_projects = [
#             project
#             for project in projects
#             if project["category"] == selected
#         ]

#     for project in filtered_projects:

#         tech = " · ".join(project["technologies"])

#         st.markdown(
#             f"""
#             <div class="portfolio-card">

#                 <div style="font-size:14px;">
#                     {project["number"]} · {project["category"]}
#                 </div>

#                 <h2>{project["title"]}</h2>

#                 <p>
#                     {project["description"]}
#                 </p>

#                 <p class="accent">
#                     {tech}
#                 </p>

#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         if project["github"] != "#":
#             st.link_button(
#                 "VIEW ON GITHUB →",
#                 project["github"]
#             )

