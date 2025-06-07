import streamlit as st
import random

st.set_page_config(page_title="Virtual SMS Phone", page_icon="📱")

# Function to generate random Indian-style phone numbers
def generate_phone_number():
    first_digit = random.choice(['7', '8', '9'])
    rest = ''.join(random.choices('0123456789', k=9))
    return f"+91{first_digit}{rest}"

# Sample message templates
templates = {
    "Greeting": "Hi! How are you doing today?",
    "Reminder": "Just a friendly reminder about our meeting tomorrow.",
    "Promotion": "Get 20% off on your next purchase! Use code SAVE20.",
    "Thank You": "Thank you for your support! We appreciate you.",
    "Appointment": "Your appointment is confirmed for 3 PM on Friday."
}

st.title("📱 Virtual SMS Simulator")

if "history" not in st.session_state:
    st.session_state.history = []

sender = generate_phone_number()
receiver = generate_phone_number()

# Sidebar with templates
st.sidebar.header("Message Templates")
selected_template = st.sidebar.selectbox("Choose a template", [""] + list(templates.keys()))

# Display virtual phone image (you can replace URL with your own image)
phone_img_url = "https://cdn-icons-png.flaticon.com/512/888/888857.png"  # simple phone icon
st.image(phone_img_url, width=100)

st.markdown(f"*From:* {sender}")
st.markdown(f"*To:* {receiver}")

# If template selected, fill text area with it
if selected_template:
    message = st.text_area("Message", value=templates[selected_template], height=120)
else:
    message = st.text_area("Message", height=120)

if st.button("Send SMS"):
    if not message.strip():
        st.error("Please enter a message!")
    else:
        st.session_state.history.append({
            "from": sender,
            "to": receiver,
            "message": message
        })
        st.success("Message sent!")

st.markdown("---")
st.subheader("📜 Message History")

if not st.session_state.history:
    st.info("No messages sent yet.")
else:
    for i, msg in enumerate(reversed(st.session_state.history), 1):
        st.markdown(
            f"{i}. From:** {msg['from']} → *To:* {msg['to']}\n\n"
            f"> {msg['message']}"
        )
        st.write("---")