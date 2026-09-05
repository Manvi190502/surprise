import streamlit as st
import textwrap

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="For Anant ♡",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# IMPORTANT HTML RENDERING FIX
# ============================================================

# Streamlit's Markdown parser can interpret indented HTML
# as a code block. This wrapper removes the indentation
# before sending HTML to Streamlit.

_original_markdown = st.markdown


def safe_markdown(content, *args, **kwargs):
    if isinstance(content, str):
        content = " ".join(textwrap.dedent(content).split())
    return _original_markdown(content, *args, **kwargs)


# Replace Streamlit's markdown function with the safe version.
st.markdown = safe_markdown


# ============================================================
# SESSION STATE
# ============================================================

if "birthday_surprise_opened" not in st.session_state:
    st.session_state.birthday_surprise_opened = False

if "love_reason" not in st.session_state:
    st.session_state.love_reason = 0


# ============================================================
# CSS
# ============================================================

def apply_styles():

    st.markdown(
        """
        <style>

        /* =====================================================
           IMPORTS
        ===================================================== */

        @import url(
            'https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&display=swap'
        );

        /* =====================================================
           ROOT
        ===================================================== */

        :root {
            --ink: #293235;
            --rose: #d84a62;
            --coral: #ef765c;
            --paper: #fff9f1;
            --paper2: #fffdf8;
            --mint: #b9ddd1;
            --sun: #f4c94e;
            --lavender: #ddd6f3;
            --shadow: rgba(41, 50, 53, 0.12);
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            overflow-x: hidden;
        }

        .stApp {
            background: #f7eee6;
            color: var(--ink);
            overflow-x: hidden;
        }

        .block-container {
            max-width: 1120px;
            padding-top: 2rem;
            padding-bottom: 5rem;
        }

        /* =====================================================
           REMOVE STREAMLIT DEFAULT ELEMENTS
        ===================================================== */

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        .stDeployButton {
            display: none;
        }

        /* =====================================================
           KEYFRAMES
        ===================================================== */

        @keyframes riseIn {
            0% {
                opacity: 0;
                transform: translateY(35px);
            }

            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            0% {
                opacity: 0;
            }

            100% {
                opacity: 1;
            }
        }

        @keyframes heartbeat {

            0%,
            100% {
                transform: scale(1);
            }

            35% {
                transform: scale(1.12);
            }

            50% {
                transform: scale(1.02);
            }

            65% {
                transform: scale(1.16);
            }
        }

        @keyframes floating {

            0%,
            100% {
                transform: translateY(0) rotate(-2deg);
            }

            50% {
                transform: translateY(-14px) rotate(2deg);
            }
        }

        @keyframes floatingReverse {

            0%,
            100% {
                transform: translateY(-7px) rotate(2deg);
            }

            50% {
                transform: translateY(10px) rotate(-2deg);
            }
        }

        @keyframes shimmer {

            0% {
                background-position: 200% center;
            }

            100% {
                background-position: -200% center;
            }
        }

        @keyframes pulseGlow {

            0%,
            100% {
                box-shadow:
                    0 0 0 rgba(216, 74, 98, 0);
            }

            50% {
                box-shadow:
                    0 0 35px rgba(216, 74, 98, 0.25);
            }
        }

        @keyframes giftBounce {

            0% {
                transform: translateY(0) scale(1);
            }

            40% {
                transform: translateY(-12px) scale(1.05);
            }

            70% {
                transform: translateY(0) scale(0.98);
            }

            100% {
                transform: translateY(0) scale(1);
            }
        }

        @keyframes lidOpen {

            0% {
                transform: rotate(0);
            }

            100% {
                transform: rotate(-18deg) translate(-10px, -45px);
            }
        }

        @keyframes sparkle {

            0% {
                opacity: 0;
                transform: scale(0);
            }

            50% {
                opacity: 1;
                transform: scale(1);
            }

            100% {
                opacity: 0;
                transform: scale(1.4);
            }
        }

        @keyframes floatHeart {

            0% {
                opacity: 0;
                transform: translateY(0) scale(0.6) rotate(0);
            }

            15% {
                opacity: 0.9;
            }

            100% {
                opacity: 0;
                transform:
                    translateY(-90vh)
                    scale(1.2)
                    rotate(25deg);
            }
        }

        @keyframes finalGlow {

            0%,
            100% {
                opacity: 0.55;
            }

            50% {
                opacity: 1;
            }
        }

        @keyframes typingCursor {

            0%,
            50% {
                border-color: var(--rose);
            }

            51%,
            100% {
                border-color: transparent;
            }
        }

        /* =====================================================
           FLOATING HEARTS
        ===================================================== */

        .heart-field {
            position: fixed;
            inset: 0;
            pointer-events: none;
            overflow: hidden;
            z-index: 1;
        }

        .heart {
            position: absolute;
            bottom: -30px;
            color: rgba(216, 74, 98, 0.45);
            font-size: 18px;
            animation: floatHeart linear infinite;
        }

        .heart:nth-child(1) {
            left: 8%;
            animation-duration: 13s;
            animation-delay: 1s;
        }

        .heart:nth-child(2) {
            left: 19%;
            animation-duration: 17s;
            animation-delay: 4s;
        }

        .heart:nth-child(3) {
            left: 31%;
            animation-duration: 14s;
            animation-delay: 2s;
        }

        .heart:nth-child(4) {
            left: 47%;
            animation-duration: 18s;
            animation-delay: 6s;
        }

        .heart:nth-child(5) {
            left: 63%;
            animation-duration: 15s;
            animation-delay: 3s;
        }

        .heart:nth-child(6) {
            left: 78%;
            animation-duration: 19s;
            animation-delay: 5s;
        }

        .heart:nth-child(7) {
            left: 91%;
            animation-duration: 16s;
            animation-delay: 7s;
        }

        /* =====================================================
           FLOATING LOVE BADGE
        ===================================================== */

        .love-float {
            position: fixed;
            right: 1.5rem;
            bottom: 1.3rem;
            z-index: 50;

            width: 108px;
            height: 108px;

            border-radius: 50%;

            display: grid;
            place-items: center;

            text-align: center;

            background:
                radial-gradient(
                    circle at 35% 25%,
                    #f78ca1,
                    var(--rose)
                );

            color: white;

            border: 2px solid var(--ink);

            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size: 1.05rem;

            line-height: 1.1;

            box-shadow:
                6px 7px 0 rgba(41, 50, 53, 0.18);

            animation:
                floating 3.2s ease-in-out infinite,
                pulseGlow 4s ease-in-out infinite;
        }

        /* =====================================================
           INTRO
        ===================================================== */

        .intro {
            text-align: center;
            padding: 5rem 1rem 4rem;

            animation:
                riseIn 1s ease-out both;
        }

        .intro-small {
            font-family:
                'DM Mono',
                monospace;

            color: var(--rose);

            letter-spacing: 0.16rem;

            font-size: 0.75rem;

            text-transform: uppercase;
        }

        .intro-heart {
            font-size: 3.2rem;

            color: var(--rose);

            animation:
                heartbeat 1.8s ease-in-out infinite;

            margin-bottom: 1rem;
        }

        .intro h1 {
            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size:
                clamp(3.2rem, 9vw, 7rem);

            line-height: 0.95;

            margin: 0.5rem 0 1.4rem;

            color: var(--ink);

            font-weight: 700;
        }

        .intro h1 span {
            color: var(--rose);

            font-style: italic;

            background:
                linear-gradient(
                    90deg,
                    var(--rose),
                    var(--coral),
                    var(--rose)
                );

            background-size: 200% auto;

            -webkit-background-clip: text;
            background-clip: text;

            color: transparent;

            animation:
                shimmer 5s linear infinite;
        }

        .intro-text {
            max-width: 620px;

            margin: auto;

            font-family:
                'DM Mono',
                monospace;

            font-size: 0.92rem;

            line-height: 1.9;
        }

        .scroll-hint {
            margin-top: 3rem;

            font-family:
                'DM Mono',
                monospace;

            font-size: 0.68rem;

            letter-spacing: 0.12rem;

            color: #777;

            animation:
                floating 2.5s ease-in-out infinite;
        }

        /* =====================================================
           PAGE SECTIONS
        ===================================================== */

        .letter-page {
            min-height: 78vh;

            box-sizing: border-box;

            padding:
                5rem
                clamp(1.2rem, 6vw, 5.5rem);

            margin:
                3rem
                calc(50% - 50vw);

            width: 100vw;

            display: flex;

            align-items: center;

            border-top:
                1px solid rgba(41, 50, 53, 0.15);

            border-bottom:
                1px solid rgba(41, 50, 53, 0.15);

            position: relative;

            overflow: hidden;
        }

        .letter-page::before {
            content: "♡";

            position: absolute;

            top: 8%;

            right: 8%;

            font-size: 8rem;

            color:
                rgba(216, 74, 98, 0.08);

            transform: rotate(15deg);

            pointer-events: none;
        }

        .page-inner {
            width: min(1050px, 100%);

            margin: auto;

            position: relative;

            z-index: 2;
        }

        .page-one {
            background:
                radial-gradient(
                    circle at 15% 20%,
                    #ffd0b9 0 10%,
                    transparent 35%
                ),
                #f8e7d9;
        }

        .page-two {
            background:
                radial-gradient(
                    circle at 82% 15%,
                    #f2d166 0 8%,
                    transparent 28%
                ),
                #e6f0dd;
        }

        .page-three {
            background:
                radial-gradient(
                    circle at 10% 85%,
                    #d5d7f4 0 9%,
                    transparent 32%
                ),
                #f4e6ee;
        }

        .page-four {
            background:
                radial-gradient(
                    circle at 85% 80%,
                    #f4b980 0 8%,
                    transparent 30%
                ),
                #eee7d4;
        }

        .page-five {
            background:
                radial-gradient(
                    circle at 20% 25%,
                    #f8d360 0 5%,
                    transparent 35%
                ),
                #e6d8ee;
        }

        .page-six {
            background:
                radial-gradient(
                    circle at 80% 20%,
                    #ffc3a8 0 6%,
                    transparent 30%
                ),
                #f8e7d9;
        }

        .page-seven {
            background:
                radial-gradient(
                    circle at 50% 15%,
                    #f8d360 0 5%,
                    transparent 35%
                ),
                #cce4dc;

            text-align: center;
        }

        /* =====================================================
           PAGE TYPOGRAPHY
        ===================================================== */

        .page-kicker {
            font-family:
                'DM Mono',
                monospace;

            color: var(--rose);

            font-size: 0.76rem;

            letter-spacing: 0.11rem;

            text-transform: uppercase;
        }

        .page-heading {
            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size:
                clamp(2.6rem, 6vw, 5.2rem);

            line-height: 1.03;

            margin:
                0.7rem 0 1.4rem;
        }

        .page-copy {
            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size:
                clamp(1.15rem, 2vw, 1.42rem);

            line-height: 1.72;

            max-width: 760px;
        }

        /* =====================================================
           TWO COLUMN
        ===================================================== */

        .page-grid {
            display: grid;

            grid-template-columns:
                repeat(
                    2,
                    minmax(0, 1fr)
                );

            gap: 2rem;

            align-items: center;
        }

        /* =====================================================
           PHOTOS
        ===================================================== */

        .photo-frame {
            height: 340px;

            overflow: hidden;

            border:
                7px solid var(--paper2);

            border-radius: 4px;

            box-shadow:
                8px 9px 0
                rgba(41, 50, 53, 0.14);

            position: relative;

            transition:
                transform 500ms ease,
                box-shadow 500ms ease;
        }

        .photo-frame::after {
            content: "";

            position: absolute;

            inset: 0;

            background:
                linear-gradient(
                    120deg,
                    transparent 20%,
                    rgba(255,255,255,0.22) 50%,
                    transparent 80%
                );

            transform:
                translateX(-120%);

            transition:
                transform 800ms ease;

            pointer-events: none;
        }

        .photo-frame:hover {
            transform:
                translateY(-10px)
                rotate(1deg)
                scale(1.015);

            box-shadow:
                13px 15px 0
                rgba(41, 50, 53, 0.16);
        }

        .photo-frame:hover::after {
            transform:
                translateX(120%);
        }

        .photo-frame img {
            width: 100%;
            height: 100%;

            object-fit: cover;

            display: block;

            transition:
                transform 800ms ease,
                filter 800ms ease;
        }

        .photo-frame:hover img {
            transform: scale(1.08);

            filter:
                saturate(1.12)
                contrast(1.02);
        }

        .cake {
            animation:
                floating 5s ease-in-out infinite;
        }

        .balloons {
            animation:
                floatingReverse 5.5s ease-in-out infinite;
        }

        .photo-caption {
            font-family:
                'DM Mono',
                monospace;

            font-size: 0.68rem;

            letter-spacing: 0.07rem;

            color: var(--rose);

            margin-top: 0.65rem;

            text-transform: uppercase;
        }

        /* =====================================================
           NOTE GRID
        ===================================================== */

        .note-grid {
            display: grid;

            grid-template-columns:
                repeat(
                    2,
                    minmax(0, 1fr)
                );

            gap: 1.1rem;
        }

        .page-note {
            background:
                rgba(
                    255,
                    253,
                    248,
                    0.9
                );

            border:
                1px solid
                rgba(
                    41,
                    50,
                    53,
                    0.18
                );

            border-radius: 5px;

            padding: 1.5rem;

            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size: 1.1rem;

            line-height: 1.62;

            box-shadow:
                5px 6px 0
                rgba(41, 50, 53, 0.09);

            transition:
                transform 280ms ease,
                box-shadow 280ms ease;
        }

        .page-note:hover {
            transform:
                translateY(-8px)
                rotate(-0.4deg);

            box-shadow:
                10px 13px 0
                rgba(41, 50, 53, 0.13);
        }

        .page-note strong {
            color: var(--rose);

            font-family:
                'DM Mono',
                monospace;

            font-size: 0.73rem;

            letter-spacing: 0.06rem;
        }

        /* =====================================================
           TIMELINE
        ===================================================== */

        .timeline {
            position: relative;

            max-width: 850px;

            margin: 2rem auto 0;
        }

        .timeline::before {
            content: "";

            position: absolute;

            left: 50%;

            top: 0;

            bottom: 0;

            width: 2px;

            background:
                rgba(
                    216,
                    74,
                    98,
                    0.3
                );

            transform:
                translateX(-50%);
        }

        .timeline-item {
            width: 45%;

            background:
                rgba(
                    255,
                    253,
                    248,
                    0.9
                );

            padding: 1.4rem;

            margin-bottom: 1.5rem;

            border:
                1px solid
                rgba(
                    41,
                    50,
                    53,
                    0.16
                );

            box-shadow:
                5px 6px 0
                rgba(
                    41,
                    50,
                    53,
                    0.08
                );

            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size: 1.08rem;

            line-height: 1.55;

            transition:
                transform 300ms ease;
        }

        .timeline-item:hover {
            transform:
                translateY(-7px);
        }

        .timeline-item:nth-child(odd) {
            margin-right: auto;
        }

        .timeline-item:nth-child(even) {
            margin-left: auto;
        }

        .timeline-date {
            font-family:
                'DM Mono',
                monospace;

            color: var(--rose);

            font-size: 0.68rem;

            letter-spacing: 0.08rem;

            margin-bottom: 0.5rem;
        }

        /* =====================================================
           LETTER
        ===================================================== */

        .personal-letter {
            max-width: 820px;

            margin: auto;

            background:
                linear-gradient(
                    135deg,
                    #fffdf8,
                    #fff7ec
                );

            border:
                1px solid
                rgba(
                    41,
                    50,
                    53,
                    0.2
                );

            border-radius: 5px;

            padding:
                clamp(
                    1.5rem,
                    4vw,
                    3.4rem
                );

            box-shadow:
                10px 11px 0
                rgba(
                    41,
                    50,
                    53,
                    0.11
                );

            position: relative;
        }

        .personal-letter::before {
            content: "♡";

            position: absolute;

            top: 15px;

            right: 22px;

            color:
                rgba(
                    216,
                    74,
                    98,
                    0.2
                );

            font-size: 3rem;
        }

        .personal-letter p {
            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size:
                clamp(
                    1.05rem,
                    1.8vw,
                    1.3rem
                );

            line-height: 1.8;

            margin:
                0 0 1.2rem;
        }

        .personal-letter .sign-off {
            color: var(--rose);

            font-style: italic;

            margin-bottom: 0;
        }

        /* =====================================================
           HEART
        ===================================================== */

        .big-heart {
            font-size: 5rem;

            line-height: 1;

            color: var(--rose);

            animation:
                heartbeat 1.7s ease-in-out infinite;
        }

        /* =====================================================
           FOREVER
        ===================================================== */

        .forever-text {
            max-width: 750px;

            margin: auto;

            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size:
                clamp(
                    1.25rem,
                    2.5vw,
                    1.65rem
                );

            line-height: 1.7;
        }

        .hindi-note {
            margin-top: 2.5rem;

            padding: 2rem 1rem;

            border-top:
                1px solid
                rgba(
                    41,
                    50,
                    53,
                    0.2
                );

            border-bottom:
                1px solid
                rgba(
                    41,
                    50,
                    53,
                    0.2
                );

            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size:
                clamp(
                    1.4rem,
                    3vw,
                    2.2rem
                );

            line-height: 1.4;
        }

        .hindi-note span {
            color: var(--rose);

            font-style: italic;
        }

        /* =====================================================
           LOVE REASONS
        ===================================================== */

        .reason-box {
            max-width: 700px;

            margin:
                2rem auto;

            padding: 2rem;

            background:
                rgba(
                    255,
                    253,
                    248,
                    0.9
                );

            border:
                1px solid
                rgba(
                    41,
                    50,
                    53,
                    0.18
                );

            box-shadow:
                7px 8px 0
                rgba(
                    41,
                    50,
                    53,
                    0.1
                );

            text-align: center;
        }

        .reason-number {
            font-family:
                'DM Mono',
                monospace;

            color: var(--rose);

            font-size: 0.7rem;

            letter-spacing: 0.1rem;
        }

        .reason-text {
            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size:
                clamp(
                    1.35rem,
                    3vw,
                    2rem
                );

            line-height: 1.45;

            margin:
                1rem 0;
        }

        /* =====================================================
           GIFT SURPRISE
        ===================================================== */

        .surprise-zone {
            text-align: center;

            padding:
                5rem 1rem;

            margin-top: 3rem;

            background:
                radial-gradient(
                    circle,
                    rgba(
                        216,
                        74,
                        98,
                        0.12
                    ),
                    transparent 65%
                );
        }

        .surprise-kicker {
            font-family:
                'DM Mono',
                monospace;

            font-size: 0.7rem;

            letter-spacing: 0.14rem;

            color: var(--rose);

            text-transform: uppercase;
        }

        .surprise-title {
            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size:
                clamp(
                    2.2rem,
                    5vw,
                    4rem
                );

            margin:
                0.7rem 0 1.5rem;
        }

        .gift-wrapper {
            width: 210px;

            height: 190px;

            margin: 2rem auto;

            position: relative;

            cursor: pointer;

            animation:
                giftBounce 2.2s
                ease-in-out infinite;
        }

        .gift-box {
            position: absolute;

            left: 20px;
            right: 20px;

            bottom: 0;

            height: 125px;

            background:
                linear-gradient(
                    135deg,
                    #d84a62,
                    #ef765c
                );

            border:
                2px solid
                var(--ink);

            border-radius: 4px;

            box-shadow:
                8px 9px 0
                rgba(
                    41,
                    50,
                    53,
                    0.17
                );
        }

        .gift-box::before {
            content: "";

            position: absolute;

            left: 50%;

            transform:
                translateX(-50%);

            top: 0;

            width: 27px;

            height: 100%;

            background:
                #f4c94e;
        }

        .gift-lid {
            position: absolute;

            left: 10px;
            right: 10px;

            top: 25px;

            height: 35px;

            background:
                #d84a62;

            border:
                2px solid
                var(--ink);

            border-radius: 4px;

            z-index: 5;
        }

        .gift-lid::after {
            content: "";

            position: absolute;

            left: 50%;

            top: 0;

            transform:
                translateX(-50%);

            width: 25px;

            height: 100%;

            background:
                #f4c94e;
        }

        .gift-ribbon {
            position: absolute;

            left: 50%;

            top: -12px;

            width: 55px;

            height: 30px;

            transform:
                translateX(-50%);
        }

        .gift-ribbon::before,
        .gift-ribbon::after {
            content: "";

            position: absolute;

            width: 28px;

            height: 25px;

            border:
                5px solid
                #f4c94e;

            border-radius:
                50% 50% 0 50%;
        }

        .gift-ribbon::before {
            left: 0;

            transform:
                rotate(-30deg);
        }

        .gift-ribbon::after {
            right: 0;

            transform:
                scaleX(-1)
                rotate(-30deg);
        }

        .gift-click {
            font-family:
                'DM Mono',
                monospace;

            font-size: 0.72rem;

            color: var(--rose);

            letter-spacing: 0.08rem;

            margin-top: 2rem;

            text-transform: uppercase;
        }

        /* =====================================================
           FINAL REVEAL
        ===================================================== */

        .final-reveal {
            text-align: center;

            padding:
                5rem 1.5rem;

            margin:
                3rem
                calc(50% - 50vw);

            width: 100vw;

            background:
                radial-gradient(
                    circle at center,
                    #343d40,
                    #1e2426 70%
                );

            color: white;

            position: relative;

            overflow: hidden;

            animation:
                fadeIn 1s ease both;
        }

        .final-reveal::before {
            content: "✦";

            position: absolute;

            top: 12%;

            left: 12%;

            font-size: 2rem;

            animation:
                sparkle 3s infinite;
        }

        .final-reveal::after {
            content: "✦";

            position: absolute;

            bottom: 15%;

            right: 15%;

            font-size: 2.5rem;

            animation:
                sparkle 4s
                1s infinite;
        }

        .final-heart {
            font-size: 5rem;

            color: #f78ca1;

            animation:
                heartbeat 1.7s
                ease-in-out
                infinite;
        }

        .final-title {
            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size:
                clamp(
                    2.5rem,
                    7vw,
                    5.5rem
                );

            line-height: 1;

            margin:
                1rem 0;
        }

        .final-message {
            max-width: 700px;

            margin:
                1.5rem auto;

            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size:
                clamp(
                    1.2rem,
                    2.5vw,
                    1.65rem
                );

            line-height: 1.7;
        }

        .final-sign {
            font-family:
                'Playfair Display',
                Georgia,
                serif;

            font-size: 1.4rem;

            color: #f7c5cf;

            font-style: italic;

            margin-top: 2rem;
        }

        /* =====================================================
           TYPEWRITER
        ===================================================== */

        .typewriter {
            display: inline-block;

            border-right:
                2px solid
                var(--rose);

            animation:
                typingCursor 0.8s
                infinite;

            padding-right: 4px;
        }

        /* =====================================================
           CONFETTI
        ===================================================== */

        .confetti {
            position: fixed;

            top: -20px;

            width: 9px;

            height: 15px;

            z-index: 100;

            pointer-events: none;

            animation:
                confettiFall 4s
                linear forwards;
        }

        @keyframes confettiFall {

            0% {
                transform:
                    translateY(0)
                    rotate(0);
                opacity: 1;
            }

            100% {
                transform:
                    translateY(110vh)
                    rotate(720deg);
                opacity: 0;
            }
        }

        /* =====================================================
           STREAMLIT BUTTON
        ===================================================== */

        div.stButton > button {
            border:
                1px solid
                var(--ink);

            border-radius: 4px;

            background:
                var(--rose);

            color: white;

            padding:
                0.8rem 1.5rem;

            font-family:
                'DM Mono',
                monospace;

            font-size: 0.75rem;

            letter-spacing: 0.05rem;

            transition:
                all 220ms ease;

            box-shadow:
                5px 6px 0
                rgba(
                    41,
                    50,
                    53,
                    0.2
                );
        }

        div.stButton > button:hover {
            transform:
                translateY(-4px);

            background:
                var(--ink);

            border-color:
                var(--ink);

            color: white;

            box-shadow:
                7px 9px 0
                rgba(
                    41,
                    50,
                    53,
                    0.18
                );
        }

        /* =====================================================
           MOBILE
        ===================================================== */

        @media (max-width: 760px) {

            .block-container {
                padding-top: 1rem;
            }

            .intro {
                padding:
                    3rem 1rem;
            }

            .letter-page {
                min-height: auto;

                padding:
                    4rem 1.2rem;

                margin-top: 2rem;
                margin-bottom: 2rem;
            }

            .page-grid,
            .note-grid {
                grid-template-columns: 1fr;
            }

            .photo-frame {
                height: 280px;
            }

            .love-float {
                width: 82px;
                height: 82px;

                right: 0.7rem;
                bottom: 0.7rem;

                font-size: 0.82rem;
            }

            .timeline::before {
                left: 12px;
            }

            .timeline-item {
                width: auto;

                margin-left: 35px !important;
                margin-right: 0 !important;
            }

            .gift-wrapper {
                transform:
                    scale(0.9);
            }

            .final-reveal {
                margin-top: 2rem;
            }
        }

        /* =====================================================
           REDUCED MOTION
        ===================================================== */

        @media (prefers-reduced-motion: reduce) {

            *,
            *::before,
            *::after {
                animation-duration: 0.001ms !important;
                animation-iteration-count: 1 !important;
                scroll-behavior: auto !important;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# APPLY CSS
# ============================================================

apply_styles()


# ============================================================
# FLOATING HEARTS
# ============================================================

st.markdown(
    """
    <div class="heart-field">
        <div class="heart">♡</div>
        <div class="heart">♥</div>
        <div class="heart">♡</div>
        <div class="heart">♥</div>
        <div class="heart">♡</div>
        <div class="heart">♥</div>
        <div class="heart">♡</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FLOATING LOVE BADGE
# ============================================================

st.markdown(
    """
    <div class="love-float">
        I love you,<br>
        bebu ♡
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# INTRO
# ============================================================

st.markdown(
    """
    <section class="intro">

        <div class="intro-heart">♡</div>

        <div class="intro-small">
            A little corner of the internet made only for you
        </div>

        <h1>
            Happy Birthday,<br>
            <span>Anant, my love.</span>
        </h1>

        <div class="intro-text">
            You make my days special, my nights sweeter,
            and ordinary life feel like my favorite movie.
            You are not just special to me.
            You are my only one.
        </div>

        <div class="scroll-hint">
            ↓ &nbsp; SCROLL SLOWLY &nbsp; ↓
        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE 01
# ============================================================

st.markdown(
    """
    <section class="letter-page page-one">

        <div class="page-inner">

            <div class="page-kicker">
                PAGE 01 / FOR MY BIRTHDAY BOY
            </div>

            <h2 class="page-heading">
                Today is about<br>
                you.
            </h2>

            <div class="page-grid">

                <div class="page-copy">
                    There are so many things I could say
                    about you, but somehow words always
                    feel smaller than what I actually feel.

                    <br><br>

                    So today, I made you a little world
                    filled with pieces of us.
                </div>

                <div>

                    <div class="photo-frame cake">

                        <img
                            src="https://images.unsplash.com/photo-1464349153735-7db50ed83c84?auto=format&fit=crop&w=1000&q=85"
                            alt="Birthday cake"
                        >

                    </div>

                    <div class="photo-caption">
                        A wish for the birthday boy
                    </div>

                </div>

            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE 02 — MEMORIES
# ============================================================

st.markdown(
    """
    <section class="letter-page page-two">

        <div class="page-inner">

            <div class="page-kicker">
                PAGE 02 / OUR LITTLE MEMORIES
            </div>

            <h2 class="page-heading">
                Every moment with you<br>
                became special.
            </h2>

            <div class="page-grid">

                <div>

                    <div class="photo-frame balloons">

                        <img
                            src="https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=1000&q=85"
                            alt="Colorful balloons"
                        >

                    </div>

                    <div class="photo-caption">
                        A little celebration for my only one
                    </div>

                </div>

                <div class="page-copy">

                    From Tambdi Surla to the beach proposal,
                    every beachside walk, evening walk,
                    CC lab moment, bike ride, hand hold,
                    and every look between us has become
                    a memory I hold close to my heart.

                    <br><br>

                    With you, even the simplest moments
                    feel magical.

                </div>

            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE 03 — LITTLE THINGS
# ============================================================

st.markdown(
    """
    <section class="letter-page page-three">

        <div class="page-inner">

            <div class="page-kicker">
                PAGE 03 / THE LITTLE THINGS
            </div>

            <h2 class="page-heading">
                Every part of you<br>
                feels like home.
            </h2>

            <div class="note-grid">

                <div class="page-note">
                    <strong>YOUR TWINKLING EYES</strong>
                    <br><br>
                    Your twinkling eyes are my favorite
                    place to get lost. One look from you
                    makes everything softer and brighter.
                </div>

                <div class="page-note">
                    <strong>YOUR EYELASHES</strong>
                    <br><br>
                    I notice your eyelashes more than
                    you know. They are one of those tiny,
                    beautiful details that are entirely you.
                </div>

                <div class="page-note">
                    <strong>YOUR SMILE & LIPS</strong>
                    <br><br>
                    Your smile changes the mood of a room.
                    I love every laugh, every soft word,
                    and every kiss that comes with it.
                </div>

                <div class="page-note">
                    <strong>YOUR NOSE & EVERYTHING</strong>
                    <br><br>
                    Your expressions, voice, quirks,
                    and your whole beautiful self.
                    I love all of you, exactly as you are.
                </div>

            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE 04 — HOW YOU LOVE ME
# ============================================================

st.markdown(
    """
    <section class="letter-page page-four">

        <div class="page-inner">

            <div class="page-kicker">
                PAGE 04 / HOW YOU LOVE ME
            </div>

            <h2 class="page-heading">
                You showed up.<br>
                Again and again.
            </h2>

            <div class="note-grid">

                <div class="page-note">

                    <strong>YOUR QUIET CARE</strong>

                    <br><br>

                    I feel it when you ask,
                    “tu thik h na?”

                    In your protectiveness,
                    tight hugs, hand holding,
                    and the way you make me laugh
                    when I am sad.

                </div>

                <div class="page-note">

                    <strong>YOUR EFFORT</strong>

                    <br><br>

                    From Tambdi Surla to coming to
                    Delhi and Mumbai to meet me,
                    you have shown me love before
                    I even knew how to ask for it.

                </div>

                <div class="page-note">

                    <strong>YOUR SUPPORT</strong>

                    <br><br>

                    You were there in my hardest time,
                    helping me speak, heal, and feel safe.

                    I will always be grateful for the
                    gentleness you gave me.

                </div>

                <div class="page-note">

                    <strong>MY PROMISE</strong>

                    <br><br>

                    I will keep falling for you every day.

                    In every chapter ahead,
                    I want it to be you and me.

                </div>

            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE 05 — TIMELINE
# ============================================================

st.markdown(
    """
    <section class="letter-page page-five">

        <div class="page-inner">

            <div class="page-kicker">
                PAGE 05 / OUR STORY
            </div>

            <h2 class="page-heading">
                From then<br>
                to forever.
            </h2>

            <div class="timeline">

                <div class="timeline-item">

                    <div class="timeline-date">
                        CHAPTER 01
                    </div>

                    From classmates...

                    <br><br>

                    ...to someone who slowly
                    became much more than that.

                </div>

                <div class="timeline-item">

                    <div class="timeline-date">
                        CHAPTER 02
                    </div>

                    Tambdi Surla.

                    <br><br>

                    One of those places that will
                    forever have a little piece of us.

                </div>

                <div class="timeline-item">

                    <div class="timeline-date">
                        CHAPTER 03
                    </div>

                    Beach walks.

                    <br><br>

                    Long conversations,
                    little silences,
                    holding hands,
                    and simply being together.

                </div>

                <div class="timeline-item">

                    <div class="timeline-date">
                        CHAPTER 04
                    </div>

                    Delhi. Mumbai.
                    All the effort.

                    <br><br>

                    Distance never stopped you
                    from showing up.

                </div>

                <div class="timeline-item">

                    <div class="timeline-date">
                        CHAPTER 05
                    </div>

                    And now...

                    <br><br>

                    I don't want just memories.

                    I want the chapters
                    we haven't lived yet.

                </div>

            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE 06 — SECRETS
# ============================================================

st.markdown(
    """
    <section class="letter-page page-four">

        <div class="page-inner">

            <div class="page-kicker">
                PAGE 06 / QUICK SECRETS
            </div>

            <h2 class="page-heading">
                A few things<br>
                I need to confess.
            </h2>

            <div class="note-grid">

                <div class="page-note">
                    <strong>SECRET 01</strong>
                    <br><br>
                    I had a little crush on you
                    from the very beginning.
                </div>

                <div class="page-note">
                    <strong>SECRET 02</strong>
                    <br><br>
                    I love you more than you
                    know I love you.
                </div>

                <div class="page-note">
                    <strong>SECRET 03</strong>
                    <br><br>
                    You have to clear out all the
                    mess I create in the future.
                    That is part of your forever
                    job now.
                </div>

                <div class="page-note">
                    <strong>SECRET 04</strong>
                    <br><br>
                    I love annoying you by hitting
                    your OCD. Your reactions are
                    honestly one of my favorite things.
                </div>

                <div class="page-note">
                    <strong>SECRET 05</strong>
                    <br><br>
                    You are the best, bebu.
                    Truly and completely.
                </div>

            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE 07 — LETTER
# ============================================================

st.markdown(
    """
    <section class="letter-page page-six">

        <div class="page-inner">

            <div class="page-kicker">
                PAGE 07 / A LETTER FROM MANUU
            </div>

            <h2 class="page-heading">
                Dear Anant,
            </h2>

            <div class="personal-letter">

                <p>
                    Wish you a very happy birthday.
                    I love you, always and forever.
                    Thank you for staying with me
                    and putting so much effort into us.
                </p>

                <p>
                    You made me realize what love
                    looks like. You made me realize
                    what love feels like.
                    You made my life story feel
                    like a fairy tale.
                </p>

                <p>
                    There were hard times, but you
                    helped me come out of them and
                    heal from that traumatic experience.
                    Thank you for tolerating my moods.
                    Thank you for being patient with me.
                    Thank you for your care and love.
                </p>

                <p>
                    From just classmates to soulmates,
                    we have made so much progress.
                    I hope we celebrate our birthdays
                    together, always and forever.
                    You are truly a very good man.
                </p>

                <p>
                    I know I look into your eyes very
                    little, because every time I do,
                    I fall more deeply and become more
                    emotional.

                    I know you want me to be more
                    expressive, but express karne ke
                    liye toh poori life bachi hai.

                    We have our whole life to understand
                    each other even more.
                </p>

                <p>
                    And I am sorry if I ever hurt you.
                    You are the best song of my life,
                    the melody that makes everything
                    feel more beautiful.
                </p>

                <p>
                    These words are still far too few
                    to express my feelings.

                    I love you, and happy birthday,
                    bebuuuuuu, once again.
                </p>

                <p class="sign-off">
                    Only and only yours,<br>
                    Manuuu ♡
                </p>

            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE 08 — REASONS
# ============================================================

reasons = [
    "Because you make ordinary days feel special.",
    "Because you ask me, “tu thik h na?” when I need it most.",
    "Because your hugs make everything feel okay.",
    "Because you make me laugh even when I don't want to.",
    "Because you always try.",
    "Because you came into my life and changed it.",
    "Because I can be completely myself with you.",
    "Because your smile is one of my favorite things.",
    "Because you understand the little things.",
    "Because somehow, out of everyone, it became you.",
]


st.markdown(
    """
    <section class="letter-page page-three">

        <div class="page-inner">

            <div class="page-kicker">
                PAGE 09 / ONE OF MANY REASONS
            </div>

            <h2 class="page-heading">
                Why I love you.
            </h2>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


reason_col1, reason_col2, reason_col3 = st.columns(
    [1, 2, 1]
)

with reason_col2:

    st.markdown(
        f"""
        <div class="reason-box">

            <div class="reason-number">
                REASON {st.session_state.love_reason + 1:02d}
                / 10
            </div>

            <div class="reason-text">
                {reasons[st.session_state.love_reason]}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "♡  GIVE ME ANOTHER REASON",
        key="another_reason",
        use_container_width=True,
    ):

        st.session_state.love_reason = (
            st.session_state.love_reason + 1
        ) % len(reasons)

        st.rerun()


# ============================================================
# PAGE 10 — FOREVER
# ============================================================

st.markdown(
    """
    <section class="letter-page page-seven">

        <div class="page-inner">

            <div class="big-heart">
                ♡
            </div>

            <div class="page-kicker">
                PAGE 10 / OUR FOREVER
            </div>

            <h2 class="page-heading">
                My wish is a life<br>
                with you.
            </h2>

            <div class="forever-text">

                I want our happy family,
                journeys still waiting for us,
                wishes fulfilled together,
                and a whole fairy-tale life with you.

                <br><br>

                <span style="color:#d84a62;">
                    तुम्हारे साथ एक खुशहाल घर,
                    अनगिनत सफ़र,
                    और पूरी ज़िंदगी चाहिए।
                </span>

            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SURPRISE SECTION
# ============================================================

st.markdown(
    """
    <div class="surprise-zone">

        <div class="surprise-kicker">
            ONE LAST THING
        </div>

        <div class="surprise-title">
            I kept something for you.
        </div>

        <div class="gift-wrapper">

            <div class="gift-ribbon"></div>

            <div class="gift-lid"></div>

            <div class="gift-box"></div>

        </div>

        <div class="gift-click">
            Press the button below ♡
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SURPRISE BUTTON
# ============================================================

button_col1, button_col2, button_col3 = st.columns(
    [1, 2, 1]
)

with button_col2:

    if st.button(
        "🎁  PRESS FOR YOUR BIRTHDAY SURPRISE  🎁",
        key="birthday_surprise",
        use_container_width=True,
    ):

        st.session_state.birthday_surprise_opened = True

        st.rerun()


# ============================================================
# FINAL SURPRISE
# ============================================================

if st.session_state.birthday_surprise_opened:

    st.balloons()

    st.markdown(
        """
        <div class="final-reveal">

            <div class="final-heart">
                ♥
            </div>

            <div class="surprise-kicker"
                 style="color:#f7c5cf;">
                SURPRISE UNLOCKED
            </div>

            <div class="final-title">
                Happy Birthday,<br>
                Anant.
            </div>

            <div class="final-message">

                <span class="typewriter">
                    You are my favorite person,
                    my safest place,
                    and my forever wish.
                </span>

                <br><br>

                I don't know what the future
                will look like...

                <br>

                but I know who I want beside me
                while we find out.

            </div>

            <div class="final-sign">
                I love you, bebu. ♡
                <br><br>
                Always yours,<br>
                Manuuu
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div style="
        text-align:center;
        padding:4rem 1rem 2rem;
        font-family:'DM Mono',monospace;
        font-size:0.65rem;
        letter-spacing:0.08rem;
        color:#777;
    ">
        MADE WITH TOO MUCH LOVE ♡
        <br><br>
        FOR ANANT
    </div>
    """,
    unsafe_allow_html=True,
)

