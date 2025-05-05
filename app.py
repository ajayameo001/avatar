import streamlit as st
import py_avataaars as pa
from PIL import Image
from random import randrange


# Avatar customization heading
st.sidebar.header('Customize your avatar')

# Avatar styles
option_style = st.sidebar.selectbox('Style', ('CIRCLE', 'TRANSPARENT'))
list_skin_color = ['TANNED','YELLOW','PALE','LIGHT','BROWN','DARK_BROWN','BLACK']
list_top_type = ['NO_HAIR','EYE_PATCH','HAT','HIJAB','TURBAN',
                 'WINTER_HAT1','WINTER_HAT2','WINTER_HAT3',
                 'WINTER_HAT4','LONG_HAIR_BIG_HAIR','LONG_HAIR_BOB',
                 'LONG_HAIR_BUN','LONG_HAIR_CURLY','LONG_HAIR_CURVY',
                 'LONG_HAIR_DREADS','LONG_HAIR_FRIDA','LONG_HAIR_FRO',
                 'LONG_HAIR_FRO_BAND','LONG_HAIR_NOT_TOO_LONG',
                 'LONG_HAIR_SHAVED_SIDES','LONG_HAIR_MIA_WALLACE',
                 'LONG_HAIR_STRAIGHT','LONG_HAIR_STRAIGHT2',
                 'LONG_HAIR_STRAIGHT_STRAND','SHORT_HAIR_DREADS_01',
                 'SHORT_HAIR_DREADS_02','SHORT_HAIR_FRIZZLE',
                 'SHORT_HAIR_SHAGGY_MULLET','SHORT_HAIR_SHORT_CURLY',
                 'SHORT_HAIR_SHORT_FLAT','SHORT_HAIR_SHORT_ROUND',
                 'SHORT_HAIR_SHORT_WAVED','SHORT_HAIR_SIDES',
                 'SHORT_HAIR_THE_CAESAR','SHORT_HAIR_THE_CAESAR_SIDE_PART']
list_hair_color = ['AUBURN','BLACK','BLONDE','BLONDE_GOLDEN','BROWN',
                   'BROWN_DARK','PASTEL_PINK','PLATINUM','RED','SILVER_GRAY']
list_hat_color = ['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02',
                  'HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE',
                  'PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
list_facial_hair_type = ['DEFAULT','BEARD_MEDIUM','BEARD_LIGHT','BEARD_MAJESTIC','MOUSTACHE_FANCY','MOUSTACHE_MAGNUM']
list_mouth_type = ['DEFAULT','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT']
list_eye_type = ['DEFAULT','CLOSE','CRY','DIZZY','EYE_ROLL','HAPPY','HEARTS','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
list_eyebrow_type = ['DEFAULT','DEFAULT_NATURAL','ANGRY','ANGRY_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL','SAD_CONCERNED','SAD_CONCERNED_NATURAL','UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
list_accessories_type = ['DEFAULT','KURT','PRESCRIPTION_01','PRESCRIPTION_02','ROUND','SUNGLASSES','WAYFARERS']
list_clothe_type = ['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
list_clothe_color = ['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
list_clothe_graphic_type = ['BAT','CUMBIA','DEER','DIAMOND','HOLA','PIZZA','RESIST','SELENA','BEAR','SKULL_OUTLINE','SKULL']


def generate_random_avatar():
    """Generate random avatar"""
    return {
        "index_skin_color": list_skin_color[randrange(0, len(list_skin_color))],
        "index_top_type": list_top_type[randrange(0, len(list_top_type))],
        "index_hair_color": list_hair_color[randrange(0, len(list_hair_color))],
        "index_hat_color": list_hat_color[randrange(0, len(list_hat_color))],
        "index_facial_hair_type": list_facial_hair_type[randrange(0, len(list_facial_hair_type))],
        "index_mouth_type": list_mouth_type[randrange(0, len(list_mouth_type))],
        "index_eye_type": list_eye_type[randrange(0, len(list_eye_type))],
        "index_eyebrow_type": list_eyebrow_type[randrange(0, len(list_eyebrow_type))],
        "index_accessories_type": list_accessories_type[randrange(0, len(list_accessories_type))],
        "index_clothe_type": list_clothe_type[randrange(0, len(list_clothe_type))],
        "index_clothe_color": list_clothe_color[randrange(0, len(list_clothe_color))],
        "index_clothe_graphic_type": list_clothe_graphic_type[randrange(0, len(list_clothe_graphic_type))],
    }

def render_avatar(avatar_config):
    """Render an avatar"""
    avatar = pa.PyAvataaar(
        style=pa.AvatarStyle.CIRCLE,
        skin_color=getattr(pa.SkinColor, str(avatar_config["index_skin_color"])),
        top_type=getattr(pa.TopType, str(avatar_config["index_top_type"])),
        hair_color=getattr(pa.HairColor, str(avatar_config["index_hair_color"])),
        facial_hair_type=getattr(pa.FacialHairType, str(avatar_config["index_facial_hair_type"])),
        mouth_type=getattr(pa.MouthType, str(avatar_config["index_mouth_type"])),
        eye_type=getattr(pa.EyesType, str(avatar_config["index_eye_type"])),
        eyebrow_type=getattr(pa.EyebrowType, str(avatar_config["index_eyebrow_type"])),
        nose_type=pa.NoseType.DEFAULT,
        accessories_type=getattr(pa.AccessoriesType, str(avatar_config["index_accessories_type"])),
        clothe_type=getattr(pa.ClotheType, str(avatar_config["index_clothe_type"])),
    )
    return avatar

# Check and save 10 random avatars in session on start-up
if "avatars" not in st.session_state:
    st.session_state.avatars = [generate_random_avatar() for _ in range(10)]

if "selected_avatar" not in st.session_state:
    st.session_state.selected_avatar = 0

# Show random 10 avatars
cols = st.columns(5)
for i, config in enumerate(st.session_state.avatars):
    avatar = render_avatar(config)
    avatar.render_png_file(f"avatar_{i}.png")
    
    with cols[i % 5]:
        st.image(f"avatar_{i}.png", use_container_width=True)
        if st.button(f"Select {i+1}"):
            st.session_state.selected_avatar = i

# Fetch selected avatar
selected_avatar = st.session_state.avatars[st.session_state.selected_avatar]

# Avatar customization options
option_skin_color = st.sidebar.selectbox('Skin color',
                                         list_skin_color,
                                         index = list_skin_color.index(selected_avatar['index_skin_color']) )

st.sidebar.subheader('Head top')
option_top_type = st.sidebar.selectbox('Head top',
                                        list_top_type,
                                        index = list_top_type.index(selected_avatar['index_top_type']))
option_hair_color = st.sidebar.selectbox('Hair color',
                                         list_hair_color,
                                         index = list_hair_color.index(selected_avatar['index_hair_color']))
option_hat_color = st.sidebar.selectbox('Hat color',
                                         list_hat_color,
                                         index = list_hat_color.index(selected_avatar['index_hat_color']))

st.sidebar.subheader('Face')
option_facial_hair_type = st.sidebar.selectbox('Facial hair type',
                                                list_facial_hair_type,
                                                index = list_facial_hair_type.index(selected_avatar['index_facial_hair_type']))
option_mouth_type = st.sidebar.selectbox('Mouth type',
                                          list_mouth_type,
                                          index = list_mouth_type.index(selected_avatar['index_mouth_type']))
option_eye_type = st.sidebar.selectbox('Eye type',
                                        list_eye_type,
                                        index = list_eye_type.index(selected_avatar['index_eye_type']))
option_eyebrow_type = st.sidebar.selectbox('Eyebrow type',
                                            list_eyebrow_type,
                                            index = list_eyebrow_type.index(selected_avatar['index_eyebrow_type']))

st.sidebar.subheader('Clothe and accessories')
option_accessories_type = st.sidebar.selectbox('Accessories type',
                                                list_accessories_type,
                                                index = list_accessories_type.index(selected_avatar['index_accessories_type']))
option_clothe_type = st.sidebar.selectbox('Clothe type',
                                           list_clothe_type,
                                           index = list_clothe_type.index(selected_avatar['index_clothe_type']))

# Configure selected avatar
avatar = pa.PyAvataaar(
    style=eval('pa.AvatarStyle.%s' % option_style),
    skin_color=eval('pa.SkinColor.%s' % option_skin_color),
    top_type=eval('pa.TopType.SHORT_HAIR_SHORT_FLAT.%s' % option_top_type),
    hair_color=eval('pa.HairColor.%s' % option_hair_color),
    facial_hair_type=eval('pa.FacialHairType.%s' % option_facial_hair_type),
    mouth_type=eval('pa.MouthType.%s' % option_mouth_type),
    eye_type=eval('pa.EyesType.%s' % option_eye_type),
    eyebrow_type=eval('pa.EyebrowType.%s' % option_eyebrow_type),
    nose_type=pa.NoseType.DEFAULT,
    accessories_type=eval('pa.AccessoriesType.%s' % option_accessories_type),
    clothe_type=eval('pa.ClotheType.%s' % option_clothe_type),
)

def image_download_button(filename, button_label="Download Avatar"):
    """Download selected avatar"""
    with open(filename, "rb") as file:
        btn = st.download_button(
            label=button_label,
            data=file,
            file_name=filename,
            mime="image/png"
        )
    return btn

# Show selected avatar
rendered_avatar = avatar.render_png_file('avatar.png')
image = Image.open('avatar.png')
st.image(image)
image_download_button("avatar.png")
