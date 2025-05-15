# import streamlit as st
# from generate import generate_slides
# from choose_template import choose_template
# from build_pptx import build_presentation

# st.set_page_config(page_title="CBRE AI PPT Generator")
# st.title("CBRE-Branded AI PowerPoint Generator")

# prompt   = st.text_input("What do you want to present?", "")
# n_slides = st.number_input("Number of slides", min_value=1, max_value=30, value=10)

# if st.button("Generate Presentation"):
#     if not prompt:
#         st.error("Please enter a topic.")
#     else:
#         with st.spinner("Generating slide content…"):
#             try:
#                 slides = generate_slides(prompt, n_slides)
#             except Exception as e:
#                 st.error(f"Content generation failed: {e}")
#                 st.stop()

#         with st.spinner("Selecting best template…"):
#             tpl = choose_template(prompt)
#             if tpl is None:
#                 st.error("Sorry, no suitable CBRE template found for your content.")
#                 st.stop()
#             st.success(f"Using template: {tpl.split('/')[-1]}")

#         with st.spinner("Building PowerPoint…"):
#             out = build_pptx(slides, tpl)

#         st.success("Presentation ready!")
#         with open(out, "rb") as f:
#             st.download_button(
#                 "Download your CBRE PPTX",
#                 data=f,
#                 file_name="CBRE_Presentation.pptx",
#                 mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
#             )


# import streamlit as st
# from generate import generate_slides
# from choose_template import choose_template
# from build_pptx import build_presentation  # ← correct import

# st.set_page_config(page_title="CBRE AI PPT Generator")
# st.title("CBRE-Branded AI PowerPoint Generator")

# prompt   = st.text_input("What do you want to present?", "")
# n_slides = st.number_input("Number of slides", min_value=1, max_value=30, value=10)

# if st.button("Generate Presentation"):
#     if not prompt:
#         st.error("Please enter a topic.")
#     else:
#         with st.spinner("Generating slide content…"):
#             try:
#                 slides = generate_slides(prompt, n_slides)
#             except Exception as e:
#                 st.error(f"Content generation failed: {e}")
#                 st.stop()

#         with st.spinner("Selecting best template…"):
#             tpl = choose_template(prompt)
#             if tpl is None:
#                 st.error("Sorry, no suitable CBRE template found for your content.")
#                 st.stop()
#             st.success(f"Using template: {tpl.split('/')[-1]}")

#         with st.spinner("Building PowerPoint…"):
#             # Use the correctly imported function name here
#             out = build_presentation(slides, tpl)

#         st.success("Presentation ready!")
#         with open(out, "rb") as f:
#             st.download_button(
#                 "Download your CBRE PPTX",
#                 data=f,
#                 file_name="CBRE_Presentation.pptx",
#                 mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
#             )

# import streamlit as st
# from generate import generate_slides
# from choose_template import choose_template
# from build_pptx import build_presentation

# st.set_page_config(page_title="CBRE AI PPT Generator", layout="centered")
# st.title("📊 CBRE-Branded AI PowerPoint Generator")

# # User Inputs
# prompt = st.text_input("💡 What do you want to present?", "")
# n_slides = st.number_input("📝 Number of slides", min_value=1, max_value=20, value=10)

# if st.button("Generate Presentation"):
#     if not prompt.strip():
#         st.error("🚫 Please enter a topic to proceed.")
#         st.stop()

#     # Step 1: Generate Slide Content
#     with st.spinner("🤖 Generating slide content…"):
#         try:
#             slides = generate_slides(prompt, n_slides)
#         except Exception as e:
#             st.error(f"❌ Content generation failed: {e}")
#             st.stop()

#     # Step 2: Choose Template (with fallback)
#     with st.spinner("🧠 Selecting best-fit CBRE template…"):
#         tpl = choose_template(prompt)
#         if tpl is None:
#             st.warning("⚠️ No exact match found. Trying to find a similar template…")
#             tpl = choose_template(prompt, allow_fallback=True)
#             if tpl is None:
#                 st.error("❌ Sorry, no suitable CBRE template found.")
#                 st.stop()
#         st.success(f"🎯 Using template: {tpl.split('/')[-1]}")

#     # Step 3: Build Presentation
#     with st.spinner("🛠️ Building your PowerPoint…"):
#         try:
#             output_path = build_presentation(slides, tpl)
#         except Exception as e:
#             st.error(f"❌ Failed to build presentation: {e}")
#             st.stop()

#     # Step 4: Download Button
#     st.success("✅ Presentation ready!")
#     with open(output_path, "rb") as f:
#         st.download_button(
#             label="⬇️ Download your CBRE Presentation",
#             data=f,
#             file_name="CBRE_Presentation.pptx",
#             mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
#         )

import streamlit as st
from generate import generate_slides
from choose_template import choose_template
from build_pptx import build_presentation

# 👇 Hide the Fork button in Streamlit Deploy
st.markdown('<style>button[kind="header"] { display: none; }</style>', unsafe_allow_html=True)

st.set_page_config(page_title="CBRE AI PPT Generator", layout="centered")
st.title("📊 CBRE-Branded AI PowerPoint Generator")

# User Inputs
prompt = st.text_input("💡 What do you want to present?", "")
n_slides = st.number_input("📝 Number of slides", min_value=1, max_value=20, value=10)

if st.button("Generate Presentation"):
    if not prompt.strip():
        st.error("🚫 Please enter a topic to proceed.")
        st.stop()

    # Step 1: Generate Slide Content
    with st.spinner("🤖 Generating slide content…"):
        try:
            slides = generate_slides(prompt, n_slides)
        except Exception as e:
            st.error(f"❌ Content generation failed: {e}")
            st.stop()

    # Step 2: Choose Template (with fallback)
    with st.spinner("🧠 Selecting best-fit CBRE template…"):
        tpl = choose_template(prompt)
        if tpl is None:
            st.warning("⚠️ No exact match found. Trying to find a similar template…")
            tpl = choose_template(prompt, allow_fallback=True)
            if tpl is None:
                st.error("❌ Sorry, no suitable CBRE template found.")
                st.stop()
        st.success(f"🎯 Using template: {tpl.split('/')[-1]}")

    # Step 3: Build Presentation
    with st.spinner("🛠️ Building your PowerPoint…"):
        try:
            output_path = build_presentation(slides, tpl)
        except Exception as e:
            st.error(f"❌ Failed to build presentation: {e}")
            st.stop()

    # Step 4: Download Button
    st.success("✅ Presentation ready!")
    with open(output_path, "rb") as f:
        st.download_button(
            label="⬇️ Download your CBRE Presentation",
            data=f,
            file_name="CBRE_Presentation.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )