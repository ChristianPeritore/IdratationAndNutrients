#include <iostream>
#include <string>
#include <map>
#include <iomanip>
#include <vector>

using namespace std;

// Struttura per contenere i testi tradotti
struct Translation {
    string title, name, weight, height, btn, surv, rec, waterFor, prot, fats, carbs, unitW, unitH, unitV;
};

// Database delle traduzioni
map<string, Translation> dict = {
    {"it", {"Nutri-Hydra Calc", "Nome", "Peso", "Altezza", "Calcola", "Minimo Sopravvivenza", "Raccomandato Mediterranea", "Acqua per", "Proteine", "Grassi", "Carboidrati", "kg", "cm", "L"}},
    {"en", {"Nutri-Hydra Calc", "Name", "Weight", "Height", "Calculate", "Minimum Survival", "Recommended Med Diet", "Water for", "Proteins", "Fats", "Carbs", "lb", "in", "gal"}},
    {"de", {"Nutri-Hydra Calc", "Name", "Gewicht", "Größe", "Berechnen", "Minimum Überleben", "Empfohlen Mittelmeer", "Wasser für", "Proteine", "Fette", "Kohlenhydrate", "kg", "cm", "L"}},
    {"fr", {"Nutri-Hydra Calc", "Nom", "Poids", "Taille", "Calculer", "Minimum Survie", "Recommandé Méditerranée", "Eau pour", "Protéines", "Lipides", "Glucides", "kg", "cm", "L"}},
    {"es", {"Nutri-Hydra Calc", "Nombre", "Peso", "Altura", "Calcular", "Mínimo Supervivencia", "Recomendado Mediterránea", "Agua para", "Proteínas", "Grasas", "Carbohidratos", "kg", "cm", "L"}}
};

void drawBar(string label, double percent, string color) {
    int width = 20;
    int pos = width * (percent / 100);
    cout << left << setw(15) << label << " [";
    for (int i = 0; i < width; ++i) {
        if (i < pos) cout << "=";
        else cout << " ";
    }
    cout << "] " << fixed << setprecision(1) << percent << "%" << endl;
}

int main() {
    string lang, userName;
    int unitChoice, sportChoice;
    double weight, height, freq = 0, hours = 0;

    // 1. Selezione Lingua
    cout << "Select Language (it, en, de, fr, es): ";
    cin >> lang;
    if (dict.find(lang) == dict.end()) lang = "en";
    Translation t = dict[lang];

    cout << "\n=== " << t.title << " ===" << endl;

    // 2. Input Dati
    cout << t.name << ": "; cin >> userName;
    cout << "1. Metric (kg/cm) | 2. Imperial (lb/in): "; cin >> unitChoice;
    cout << t.weight << " (" << (unitChoice == 1 ? "kg" : "lb") << "): "; cin >> weight;
    cout << t.height << " (" << (unitChoice == 1 ? "cm" : "in") << "): "; cin >> height;
    cout << "Sport? (1: Yes, 0: No): "; cin >> sportChoice;

    if (sportChoice == 1) {
        cout << "Times/Week: "; cin >> freq;
        cout << "Hours/Session: "; cin >> hours;
    }

    // 3. Logica di Calcolo (Base Metrica)
    double calcWeight = (unitChoice == 2) ? weight * 0.453592 : weight;
    double sportAddon = (sportChoice == 1) ? (freq * hours * 0.7) / 7.0 : 0;

    double waterRec = (calcWeight * 0.035) + sportAddon;
    double waterSurv = (calcWeight * 0.025) + (sportAddon * 0.5);
    double prot = calcWeight * (sportChoice == 1 ? 1.6 : 1.2);
    double fats = calcWeight * 0.9;
    double carbs = calcWeight * 3.5;

    // Conversione volume se Imperiale
    double volConv = (unitChoice == 2) ? 0.264172 : 1.0;
    string volUnit = (unitChoice == 2) ? " gal" : " L";

    // 4. Output Risultati
    cout << "\n" << string(40, '-') << endl;
    cout << t.waterFor << " " << userName << ":" << endl;
    cout << "[!] " << t.surv << ": " << fixed << setprecision(2) << waterSurv * volConv << volUnit << endl;
    cout << "[*] " << t.rec << ": " << waterRec * volConv << volUnit << endl;
    cout << string(40, '-') << endl;

    cout << t.prot << ": " << (int)prot << "g" << endl;
    cout << t.fats << ": " << (int)fats << "g" << endl;
    cout << t.carbs << ": " << (int)carbs << "g" << endl;

    // 5. "Grafico" Testuale (Percentuali)
    double totalMacros = prot + fats + carbs;
    cout << "\n--- MACRONUTRIENT DISTRIBUTION ---" << endl;
    drawBar(t.prot, (prot / totalMacros) * 100, "");
    drawBar(t.fats, (fats / totalMacros) * 100, "");
    drawBar(t.carbs, (carbs / totalMacros) * 100, "");

    return 0;
}