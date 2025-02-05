import streamlit as st

# 设置网页标题 & 背景颜色
st.set_page_config(page_title="❤️ 冒爱心特效", page_icon="❤️", layout="wide")

# 使用 HTML + CSS + JS 实现爱心漂浮动画
st.markdown("""
    <style>
    body {
        background-color: black;
    }
    .heart {
        position: absolute;
        color: red;
        font-size: 30px;
        animation: float 5s infinite;
    }
    @keyframes float {
        0% { transform: translateY(0); opacity: 1; }
        50% { opacity: 0.8; }
        100% { transform: translateY(-800px); opacity: 0; }
    }
    </style>
    <script>
    function createHeart() {
        let heart = document.createElement("div");
        heart.innerHTML = "❤️";
        heart.classList.add("heart");
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.animationDuration = Math.random() * 3 + 2 + "s";
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 5000);
    }
    setInterval(createHeart, 300);
    </script>
""", unsafe_allow_html=True)

# 显示网页标题
st.markdown("<h1 style='text-align: center; color: pink;'>❤️ 欢迎来到冒爱心网页 ❤️</h1>", unsafe_allow_html=True)
