import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Mina Youssef Portfolio", page_icon="💼", layout="wide")

# 2. التصميم (CSS) - شكل مودرن وأنيميشن
st.markdown("""
    <style>
    /* الخلفية العامة */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    
    /* إخفاء القوائم الافتراضية لستريمليت */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* تصميم النصوص */
    h1, h2, h3 {
        color: #00f3ff !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
    }
    
    p, li {
        color: #e0e0e0 !important;
        font-size: 18px;
    }

    /* تصميم الكروت (Cards) للمشاريع والمهارات */
    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(0, 243, 255, 0.3);
        border-color: #00f3ff;
    }

    /* تصميم الأزرار */
    .stButton>button {
        background-color: transparent;
        color: #00f3ff;
        border: 2px solid #00f3ff;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #00f3ff;
        color: #0f0c29;
        box-shadow: 0 0 15px #00f3ff;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. القسم الأول: الواجهة الرئيسية
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<h1>Hi, I'm Mina Youssef Kamal 👋</h1>", unsafe_allow_html=True)
    st.markdown("<h3>AI & IoT Engineer | Python Developer</h3>", unsafe_allow_html=True)
    st.markdown("<p>أنا مهندس متخصص في إنترنت الأشياء (IoT) والذكاء الاصطناعي. بحب أحول الأفكار المعقدة لمنتجات ذكية بتساعد البشر وتحسن البيئة. أهلاً بيك في البورتفوليو بتاعي.</p>", unsafe_allow_html=True)
    
    # أزرار التواصل
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        with col_btn1:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/zicola2019-netzen)")
    with col_btn2:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mina-youssef-zicola)")
    with col_btn3:
        st.markdown("[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Zicola2019@gmail.com)")

with col2:
    # تقدر تحط صورتك هنا بدل الإيموجي لو حبيت
    st.markdown("<h1 style='text-align: center; font-size: 150px;'>👨‍💻</h1>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==========================================
# 4. القسم الثاني: من أنا (About Me)
# ==========================================
st.markdown("<h2>👨‍💻 About Me</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <p>طالب هندسة شغوف ببناء أنظمة متكاملة (End-to-End Systems). بدأت رحلتي بالبرمجة بـ Python، ودخلت في عالم الـ IoT والذكاء الاصطناعي. بقدر أربط بين الهاردوير (زي ESP32) والسوفتوير (زي Streamlit و ThingSpeak)، وأستخدم الذكاء الاصطناعي (LLMs) عشان أحلل البيانات وأطلع قرارات ذكية.</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 5. القسم الثالث: المهارات (Skills)
# ==========================================
st.markdown("<h2>🛠️ Tech Stack</h2>", unsafe_allow_html=True)

col_sk1, col_sk2, col_sk3 = st.columns(3)

with col_sk1:
    st.markdown("""
    <div class="card">
        <h4 style='color: white;'>Languages</h4>
        <ul>
            <li>Python</li>
            <li>C++ (Arduino)</li>
            <li>SQL</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_sk2:
    st.markdown("""
    <div class="card">
        <h4 style='color: white;'>Hardware & IoT</h4>
        <ul>
            <li>ESP32 / Arduino</li>
            <li>Sensors Integration</li>
            <li>ThingSpeak / Firebase</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_sk3:
    st.markdown("""
    <div class="card">
        <h4 style='color: white;'>Software & AI</h4>
        <ul>
            <li>Streamlit</li>
            <li>Machine Learning</li>
            <li>Groq / Gemini API</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 6. القسم الرابع: المشاريع (Projects)
# ==========================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2>🚀 Featured Projects</h2>", unsafe_allow_html=True)

# مشروعك الأساسي
st.markdown("""
<div class="card">
    <h3>🏢 Humanity & Environmental Command Center</h3>
    <p><strong>An IoT-based Smart Safety System</strong></p>
    <p>نظام متكامل لمراقبة صحة العمال والبيئة المحيطة. بيعتمد على ESP32 بيبعت بيانات الحساسات (حرارة، غاز، نبضات) لسيرفر ThingSpeak. تم بناء Dashboard تفاعلية بـ Streamlit فيها خريطة GPS، وتم دمج الذكاء الاصطناعي (Llama 3) لتحليل البيانات وكتابة تقارير وتوصيات طبية فورية، مع نظام تنبيه طوارئ يبعت رسالة واتساب بالموقع.</p>
    <p><strong>Tech Stack:</strong> Python, ESP32, ThingSpeak, Streamlit, Plotly, Folium, Groq API.</p>
    <a href="https://humanity-environmental-station-kd2pbxknqecj97ylkk7dpa.streamlit.app/" target="_blank"><button style="background-color: #00f3ff; color: black; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">Live Demo 🚀</button></a>
</div>
""", unsafe_allow_html=True)

# المشروع التاني: Smart Wearable
st.markdown("""
<div class="card">
    <h3>⌚ Smart Wearable Health Ecosystem (Digital Twin)</h3>
    <p><strong>Interactive Health Monitoring & AI Diagnostics Demo</strong></p>
    <p>نظام ذكي متكامل يحاكي عمل الساعات الذكية (Smartwatches) وتطبيقات الهواتف. يعرض قراءات حية لمعدل ضربات القلب ونسبة الأكسجين (SpO2) مع رسومات بيانية تفاعلية (Live Charts). النظام مزود بذكاء اصطناعي (AI Assistant) يقدم توصيات فورية بناءً على حالة المستخدم (نوم، إجهاد، سقوط)، مع نظام تنبيه طوارئ يرسل رسالة واتساب (WhatsApp SOS) في الحالات الحرجة.</p>
    <p><strong>Tech Stack:</strong> Python, Streamlit, HTML/CSS/JS, Chart.js, AI Integration.</p>
    <a href="https://health-wearable-zkab5zpnyfvxty6hy35984.streamlit.app/" target="_blank"><button style="background-color: #00f3ff; color: black; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">Live Wearable Demo 🚀</button></a>
</div>
""", unsafe_allow_html=True)
# ==========================================
# 7. الفوتر
# ==========================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Designed & Built with ❤️ using Streamlit by Mina Youssef</p>", unsafe_allow_html=True)
