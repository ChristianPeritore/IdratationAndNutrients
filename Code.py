import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class NutriHydraApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurazione Finestra
        self.title("Nutri-Hydra Calc Pro")
        self.geometry("600x850")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Database Traduzioni
        self.translations = {
            "it": {"title": "Nutri-Hydra Calc", "name": "Nome", "weight": "Peso", "height": "Altezza", "btn": "Calcola", "surv": "Sopravvivenza", "rec": "Mediterranea", "prot": "Proteine", "fats": "Grassi", "carbs": "Carboidrati", "water": "Acqua"},
            "en": {"title": "Nutri-Hydra Calc", "name": "Name", "weight": "Weight", "height": "Height", "btn": "Calculate", "surv": "Survival", "rec": "Med Diet", "prot": "Proteins", "fats": "Fats", "carbs": "Carbs", "water": "Water"},
            "de": {"title": "Nutri-Hydra Calc", "name": "Name", "weight": "Gewicht", "height": "Größe", "btn": "Berechnen", "surv": "Überleben", "rec": "Mittelmeer", "prot": "Proteine", "fats": "Fette", "carbs": "Kohlenhydrate", "water": "Wasser"},
            "fr": {"title": "Nutri-Hydra Calc", "name": "Nom", "weight": "Poids", "height": "Taille", "btn": "Calculer", "surv": "Survie", "rec": "Méditerranée", "prot": "Protéines", "fats": "Lipides", "carbs": "Glucides", "water": "Eau"},
            "es": {"title": "Nutri-Hydra Calc", "name": "Nombre", "weight": "Peso", "height": "Altura", "btn": "Calcular", "surv": "Supervivencia", "rec": "Mediterránea", "prot": "Proteínas", "fats": "Grasas", "carbs": "Carbohidratos", "water": "Agua"}
        }

        self.setup_ui()

    def setup_ui(self):
        # Header: Lingua e Unità
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(pady=20, padx=20, fill="x")

        self.lang_menu = ctk.CTkOptionMenu(self.header_frame, values=["it", "en", "de", "fr", "es"], command=self.update_labels)
        self.lang_menu.pack(side="left", padx=5)
        self.lang_menu.set("it")

        self.unit_menu = ctk.CTkOptionMenu(self.header_frame, values=["Metric (kg/cm)", "Imperial (lb/in)"])
        self.unit_menu.pack(side="left", padx=5)

        # Form
        self.main_label = ctk.CTkLabel(self, text="Nutri-Hydra Calc", font=("Arial", 26, "bold"))
        self.main_label.pack(pady=10)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Nome", width=300)
        self.name_entry.pack(pady=5)

        self.weight_entry = ctk.CTkEntry(self, placeholder_text="Peso", width=300)
        self.weight_entry.pack(pady=5)

        self.height_entry = ctk.CTkEntry(self, placeholder_text="Altezza", width=300)
        self.height_entry.pack(pady=5)

        self.sport_check = ctk.CTkCheckBox(self, text="Pratico Sport")
        self.sport_check.pack(pady=10)

        self.calc_btn = ctk.CTkButton(self, text="Calcola", command=self.calculate, font=("Arial", 16, "bold"))
        self.calc_btn.pack(pady=20)

        # Area Risultati
        self.res_frame = ctk.CTkFrame(self)
        self.res_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Grafico
        self.figure = Figure(figsize=(4, 4), dpi=100, facecolor='#2b2b2b')
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.res_frame)
        self.canvas.get_tk_widget().pack(pady=10, fill="both", expand=True)

    def update_labels(self, lang):
        t = self.translations[lang]
        self.main_label.configure(text=t["title"])
        self.calc_btn.configure(text=t["btn"])
        self.sport_check.configure(text=t["rec"]) # Esempio di aggiornamento dinamico

    def calculate(self):
        lang = self.lang_menu.get()
        t = self.translations[lang]
        is_metric = "Metric" in self.unit_menu.get()

        try:
            w = float(self.weight_entry.get())
            # Conversione interna
            calc_w = w if is_metric else w * 0.453592
            is_sporty = self.sport_check.get()

            # Logica Nutrizionale
            water_rec = (calc_w * 0.035) + (0.7 if is_sporty else 0)
            prot = calc_w * (1.6 if is_sporty else 1.2)
            fats = calc_w * 0.9
            carbs = calc_w * 3.5

            self.update_chart(t, prot, fats, carbs, water_rec * 100)
        except ValueError:
            pass

    def update_chart(self, t, p, f, c, w):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        labels = [t["prot"], t["fats"], t["carbs"], t["water"]]
        sizes = [p, f, c, w/10] # Scalato per il grafico
        colors = ['#e74c3c', '#f1c40f', '#2ecc71', '#3498db']
        
        # Plot
        wedges, texts, autotexts = ax.pie(sizes, labels=None, autopct='%1.1f%%', 
                                        startangle=140, colors=colors, 
                                        textprops={'color':"w", 'weight':'bold'})
        
        ax.legend(wedges, labels, title="Nutrienti", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        self.canvas.draw()

if __name__ == "__main__":
    app = NutriHydraApp()
    app.mainloop()