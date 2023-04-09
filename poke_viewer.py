from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox

# Create the window
root = Tk()
root.title("Pokemon Info Viewer")
root.resizable(False, False)

# Add frames to window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, sticky=N, padx=(10, 0))

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, sticky=N, padx=10, pady=(0, 10))

# Add widgets to top frame
lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=0)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=10)

def handle_get_info_btn_click():
    # Get the name of the pokemon
    poke_name = ent_name.get().strip()
    if poke_name == '':
        return

    # Get the Pokemon info from the PokeAPI
    poke_info = get_pokemon_info(poke_name)

    if poke_info is None:
        err_msg = f"Unable to get information from the PokeAPI for {poke_name}."
        messagebox.showinfo(title='Error', message=err_msg, icon='error')
        return

    # Populate the info values
    lbl_height_value['text'] = f"{poke_info['height']} dm"
    lbl_weight_value['text'] = f"{poke_info['weight']} hg"

    types = []
    counter = 0
    for _ in poke_info['types']:
        types.append((poke_info['types'][counter]['type']['name'].title()))
        counter += 1
        
    lbl_type_value['text'] = ', '.join(types)

    # Populate the stat values
    prg_hp['value'] = poke_info['stats'][0]['base_stat']
    prg_attack['value'] = poke_info['stats'][1]['base_stat']
    prg_defense['value'] = poke_info['stats'][2]['base_stat']
    prg_special_attack['value'] = poke_info['stats'][3]['base_stat']
    prg_special_defense['value'] = poke_info['stats'][4]['base_stat']
    prg_speed['value'] = poke_info['stats'][5]['base_stat']

    return

btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info_btn_click)
btn_get_info.grid(row=0, column=2)

# Add widgets to bottom left frame
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, sticky=E)
lbl_height_value = ttk.Label(frm_btm_left, text='TBD')
lbl_height_value.grid(row=0, column=1, sticky=W)

lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, sticky=E)
lbl_weight_value = ttk.Label(frm_btm_left, text='TBD')
lbl_weight_value.grid(row=1, column=1, sticky=W)

lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, sticky=E)
lbl_type_value = ttk.Label(frm_btm_left, text='TBD')
lbl_type_value.grid(row=2, column=1, sticky=W)

# Add widgets to bottom right frame
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, sticky=E)
prg_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_hp.grid(row=0, column=1, padx=(0, 5))

lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, sticky=E)
prg_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_attack.grid(row=1, column=1, pady=5, padx=(0, 5))

lbl_defense = ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0, sticky=E, pady=(0, 5))
prg_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_defense.grid(row=2, column=1, pady=(0, 5), padx=(0, 5))

lbl_special_attack = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_special_attack.grid(row=3, column=0, sticky=E, pady=(0, 5))
prg_special_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_special_attack.grid(row=3, column=1, pady=(0, 5), padx=(0, 5))

lbl_special_defense = ttk.Label(frm_btm_right, text='Special Defense:')
lbl_special_defense.grid(row=4, column=0, sticky=E, pady=(0, 5))
prg_special_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_special_defense.grid(row=4, column=1, pady=(0, 5), padx=(0, 5))

lbl_speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0, sticky=E, pady=(0, 5))
prg_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_speed.grid(row=5, column=1, pady=(0, 5), padx=(0, 5))


# Loop until window is closed
root.mainloop()