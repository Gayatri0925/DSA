import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mini Calculator of Data Structures", page_icon="🧮", layout="wide")

st.title("🧮 Mini Calculator of Data Structures")
st.caption("An interactive visualizer for Stack, Queue, and Linked List")

# --- Initialize session state ---
if 'stack' not in st.session_state:
    st.session_state.stack = []

if 'queue' not in st.session_state:
    st.session_state.queue = []

if 'linked_list' not in st.session_state:
    st.session_state.linked_list = []

# --- Helper Functions ---
def draw_stack(stack):
    fig, ax = plt.subplots(figsize=(2, len(stack) * 0.6))
    for i, val in enumerate(reversed(stack)):
        ax.text(0.5, i, f"{val}", ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.3", fc="#00b4d8", ec="black", lw=2))
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.5, len(stack))
    ax.axis('off')
    st.pyplot(fig)

def draw_queue(queue):
    fig, ax = plt.subplots(figsize=(len(queue) * 1, 1.5))
    for i, val in enumerate(queue):
        ax.text(i, 0, f"{val}", ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.3", fc="#90be6d", ec="black", lw=2))
    ax.set_xlim(-0.5, len(queue))
    ax.set_ylim(-0.5, 1)
    ax.axis('off')
    st.pyplot(fig)

def draw_linked_list(ll):
    fig, ax = plt.subplots(figsize=(len(ll) * 1.5, 1.5))
    for i, val in enumerate(ll):
        ax.text(i * 1.5, 0, f"{val}", ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.3", fc="#f9c74f", ec="black", lw=2))
        if i < len(ll) - 1:
            ax.arrow(i * 1.5 + 0.4, 0, 0.7, 0, head_width=0.1, head_length=0.2, fc='black', ec='black')
    ax.axis('off')
    st.pyplot(fig)

# --- Tabs for each DS ---
tab1, tab2, tab3 = st.tabs(["🧱 Stack", "🚶‍♀️ Queue", "🔗 Linked List"])

# --- STACK TAB ---
with tab1:
    st.subheader("🧱 Stack (LIFO)")
    val = st.text_input("Enter a value to push", key="stack_val")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Push"):
            if val.strip():
                try:
                    st.session_state.stack.append(int(val))
                except ValueError:
                    st.warning("Please enter a valid integer!")
    with c2:
        if st.button("Pop"):
            if st.session_state.stack:
                st.session_state.stack.pop()
    if st.session_state.stack:
        draw_stack(st.session_state.stack)
    else:
        st.info("Stack is empty!")

# --- QUEUE TAB ---
with tab2:
    st.subheader("🚶‍♀️ Queue (FIFO)")
    val = st.text_input("Enter a value to enqueue", key="queue_val")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Enqueue"):
            if val.strip():
                try:
                    st.session_state.queue.append(int(val))
                except ValueError:
                    st.warning("Please enter a valid integer!")
    with c2:
        if st.button("Dequeue"):
            if st.session_state.queue:
                st.session_state.queue.pop(0)
    if st.session_state.queue:
        draw_queue(st.session_state.queue)
    else:
        st.info("Queue is empty!")

# --- LINKED LIST TAB ---
with tab3:
    st.subheader("🔗 Linked List")
    val = st.text_input("Enter value to insert", key="ll_val")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Insert at End"):
            if val.strip():
                try:
                    st.session_state.linked_list.append(int(val))
                except ValueError:
                    st.warning("Please enter a valid integer!")
    with c2:
        if st.button("Delete Last"):
            if st.session_state.linked_list:
                st.session_state.linked_list.pop()
    with c3:
        if st.button("Clear List"):
            st.session_state.linked_list.clear()
    if st.session_state.linked_list:
        draw_linked_list(st.session_state.linked_list)
    else:
        st.info("Linked List is empty!")

st.markdown("---")
st.markdown("👩‍💻 *Created by [K. Gayatri](https://github.com/Gayatri0925) | Final Year CSE | RGM College*")
