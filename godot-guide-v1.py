import streamlit as st
from typing import Dict, List

st.set_page_config(
    page_title="Godot 4.7 Changelog Explorer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚀 Godot 4.7 Changelog Explorer")
st.markdown("**Released:** 2026-06-18 | Interactive Guide")

# Search
search_term = st.text_input("🔍 Search changelog", placeholder="Type keywords like TileMap, Jolt, vertex snap, AnimationTree...")

# Sidebar navigation
st.sidebar.header("Categories")
categories_list = [
    "2D", "3D", "Animation", "AssetLib", "Audio", "Buildsystem", "C#",
    "Codestyle", "Core", "Documentation", "Editor", "Export", "GDExtension",
    "GDScript", "GUI", "I18n", "Import", "Input", "Navigation", "Network",
    "Particles", "Physics", "Platforms", "Plugin", "Rendering", "Shaders",
    "Tests", "Thirdparty", "XR"
]

selected_category = st.sidebar.selectbox("Jump to category", ["All"] + categories_list)

# Data - Organized changelog
changelog_data: Dict[str, List[str]] = {
    "2D": [
        "Add a scene painter tool (GH-109360)",
        "Add moving and ratio-locked scaling to the region editor (GH-117835)",
        "Allow changing the color of canvas selection (GH-104860)",
        "Preview random tiles when painting (GH-118315)",
        "Rework TileSet editor proxy objects (GH-117574)",
        "Fix first tile not being randomized (GH-120085)",
        "Fix TileMap editor inconsistent Property Names (GH-117534)"
    ],
    "3D": [
        "Add vertex snapping to the 3D editor (GH-117235)",
        "Add trackball-style rotation for 3D transform gizmo (GH-109976)",
        "Create a proper editor for MeshLibrary (GH-117376)",
        "Add \"Follow Selection\" in the 3D editor (GH-99499)",
        "Add automatic smoothing for CSG nodes (GH-116749)",
        "Add vertex snap support for subgizmo points (GH-117922)",
        "Many GridMap editor improvements and fixes"
    ],
    "Animation": [
        "Add SyncMode::CYCLIC to BlendSpace1D and BlendSpace2D (GH-117275)",
        "Add ping-pong playback support to SpriteFrames (GH-114556)",
        "Add undo/redo to adding/removing StateMachine nodes (GH-116946)",
        "Optimize Animation Resource, Library, Mixer, and Player (GH-116394)",
        "Fix many AnimationTree and BlendSpace issues"
    ],
    "Editor": [
        "Add H keyboard shortcut to toggle node visibility (GH-104628)",
        "Add EditorInterface::get_unsaved_scenes() (GH-113767)",
        "Massive GridMap and MeshLibrary editor overhaul",
        "Improve inspector, docks, and theme system",
        "Add support for copy/paste of section/category properties"
    ],
    "Rendering": [
        "Add Rectangular Area Light Source (GH-108219)",
        "Implement DrawableTextures (GH-105701)",
        "Many fixes for Vulkan, D3D12, Mobile & Compatibility renderers",
        "Add bent normal map support for Compatibility renderer",
        "HDR output improvements across platforms"
    ],
    "Physics": [
        "Jolt Physics updated to 5.5.0",
        "Many Jolt integration fixes and improvements",
        "Add one-way collision direction for CollisionShape2Ds"
    ],
    # Add more categories as needed...
}

# Display logic
if selected_category == "All":
    for cat, items in changelog_data.items():
        with st.expander(f"**{cat}** ({len(items)} changes)", expanded=True):
            filtered = [item for item in items if search_term.lower() in item.lower()]
            for item in filtered:
                if "Add" in item or "Implement" in item:
                    st.success(f"✅ {item}")
                elif "Fix" in item:
                    st.info(f"🔧 {item}")
                else:
                    st.write(f"• {item}")
else:
    items = changelog_data.get(selected_category, [])
    filtered = [item for item in items if search_term.lower() in item.lower()]
    st.subheader(selected_category)
    for item in filtered:
        if "Add" in item or "Implement" in item:
            st.success(f"✅ {item}")
        elif "Fix" in item:
            st.info(f"🔧 {item}")
        else:
            st.write(f"• {item}")

# Full raw changelog in a tab
tab1, tab2 = st.tabs(["📋 Full Raw Changelog", "ℹ️ About"])

with tab1:
    st.markdown("""
    **Full Godot 4.7 Changelog** (excerpt - full version available in Godot repository)

    ### 2D
    - Add a scene painter tool...
    - ... (complete list as provided)
    """)

with tab2:
    st.info("""
    This is an interactive Streamlit explorer for **Godot 4.7**.

    **Features:**
    - Live search across all entries
    - Category navigation
    - Visual distinction between new features and fixes
    - Mobile-friendly

    Deploy this app easily on [Streamlit Community Cloud](https://share.streamlit.io).
    """)

st.caption("Made for Godot users • Python 3.12+ & Streamlit")
