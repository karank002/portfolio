import streamlit as st
from components.projects import projects_section
from components.data_lab import data_lab_section

st.set_page_config(
    page_title = "Karan Singh | Data Science",
    page_icon="📊",
    layout="wide",
)
# st.title("Karan Singh")
# st.subheader("Data Science student")

# st.write(
#     "Building projects in Data Science, Machine Learning, "
#     "Big Data and Backend Systems."
# )

with open ("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", 
        unsafe_allow_html=True)

# hero 
st.markdown(
    "<div class='hero'>"

    "<div class='profile-wrapper'>"

        "<div class='profile-frame'>"

            "<div class='profile-placeholder'>"
                "YOUR<br>"
                "PHOTO"
            "</div>"

        "</div>"

    "</div>"

    "<div class='hero-star'>"
        "✦"
    "</div>"

    "<div class='star'>"
        "✦"
    "</div>"


    "<div class='hero-decoration'>"
        "───────── ✦ ─────────"
    "</div>"

    "<h1>"
        "KARAN "
        "<span class='accent'>SINGH</span>"
    "</h1>"

    "<div class='hero-subtitle'>"
        "DATA SCIENCE STUDENT"
    "</div>"

    "<p class='hero-description'>"
        "I explore data, build intelligent systems, "
        "and turn ideas into practical projects."
    "</p>"

    "<div>"
        "<span class='spark'>✦</span>"
        "&nbsp;&nbsp;"
        "<span class='lavender'>PYTHON</span>"
        "&nbsp; · &nbsp;"
        "<span class='blue'>DATA</span>"
        "&nbsp; · &nbsp;"
        "<span class='accent'>ML</span>"
        "&nbsp;&nbsp;"
        "<span class='spark'>✦</span>"
    "</div>"

    "</div>",
    unsafe_allow_html=True
)



col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 EXPLORE MY WORK"):
        st.session_state["section"] = "projects"

with col2:
    st.button("📄 RESUME")

with col3:
    st.link_button(
        "🐙 GITHUB",
        "https://github.com/karank002"
    )

st.markdown("---")

st.markdown(
    """
    <h2>
        ABOUT <span class="accent">ME</span>
    </h2>
    """,
    unsafe_allow_html=True
)




st.markdown(
    """
    <div class="portfolio-card">

    I'm a third-year Computer Science and Engineering
    student specializing in Data Science.

    <br><br>

    I'm interested in Data Analytics, Machine Learning,
    Big Data and building practical software systems.

    <br><br>

    Currently, I'm focused on strengthening my foundations,
    building projects and exploring how data can be turned
    into useful insights.

    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<div class='portfolio-card' style='text-align:center;'>"
    "<span class='accent'>✦ CURRENTLY EXPLORING</span>"
    "<br><br>"
    "Python &nbsp; · &nbsp; "
    "Data Analytics &nbsp; · &nbsp; "
    "Machine Learning &nbsp; · &nbsp; "
    "Big Data"
    "</div>",
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        '<div class="portfolio-card"><h3>🎓</h3>'
        '<b>3rd Year</b><br>CSE</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="portfolio-card"><h3>📊</h3>'
        '<b>Data Science</b><br>Specialization</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="portfolio-card"><h3>🐍</h3>'
        '<b>Python</b><br>Data & ML</div>',
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        '<div class="portfolio-card"><h3>🧠</h3>'
        '<b>Learning</b><br>Every day</div>',
        unsafe_allow_html=True
    )

st.markdown("---")

st.markdown(
    """
    <h2>
        MY <span class="accent">SKILLS</span>
    </h2>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3, tab4 = st.tabs(
    ["PROGRAMMING", "DATA SCIENCE", "ML", "BIG DATA"]
)

with tab1:

    st.markdown(
        """
        ### 💻 Programming

        `Python`  
        `C++`  
        `Java`  
        `SQL`
        """
    )

with tab2:

    st.markdown(
        """
        ### 📊 Data Science

        `Pandas`  
        `NumPy`  
        `Matplotlib`  
        `Seaborn`
        """
    )

with tab3:

    st.markdown(
        """
        ### 🤖 Machine Learning

        `Scikit-learn`  
        `Regression`  
        `Classification`  
        `Feature Engineering`
        """
    )

with tab4:

    st.markdown(
        """
        ### 🐘 Big Data

        `Hadoop`  
        `Spark`  
        `Cassandra`
        """
    )

st.markdown("---")

projects_section()


st.markdown("---")

data_lab_section()


# import streamlit as st

# st.set_page_config(
#     page_title="Karan Singh | Data Science",
#     page_icon="📊",
#     layout="wide"
# )

# # CSS
# with open("assets/styles.css", "r") as f:
#     css = f.read()

# st.markdown(
#     f"<style>{css}</style>",
#     unsafe_allow_html=True
# )

# # HERO
