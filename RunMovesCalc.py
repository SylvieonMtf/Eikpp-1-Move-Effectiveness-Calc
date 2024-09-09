from PyQt5.QtWidgets import QApplication, QWidget
from MovesCalc import Ui_Form

class MoveEffectivenessCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.effectiveness_chart = {
            'fighting': {'grass': 0.5, 'steel': 0, 'rock': 0.5}, 
            'ground': {'ground': 0.5, 'ice': 0.5, 'fire': 2, 'normal': 2, 'poison': 2, 'grass': 0.5, 'psychic': 0.5, 'rock': 2}, 
            'ice': {'ground': 2, 'ice': 0.5, 'fire': 0.5, 'electric': 2, 'grass': 2, 'psychic': 0.5}, 
            'fairy': {'ice': 2, 'fairy': 0.5, 'fire': 0.5, 'electric': 0, 'dragon': 2, 'psychic': 0.5}, 
            'fire': {'ground': 0.5, 'ice': 2, 'fire': 0.5, 'flying': 0.5, 'electric': 2, 'dragon': 0.5, 'poison': 0.5, 'grass': 2, 'psychic': 0.5, 'rock': 0.5}, 
            'normal': {'ground': 0.5, 'ice': 0.5, 'fire': 2, 'normal': 0.5, 'electric':2, 'dragon': 2, 'psychic': 2, 'rock': 2}, 
            'dark': {'fighting': 2, 'normal': 2, 'flying': 0.5, 'dragon': 0.5, 'ghost': 0.5, 'poison': 0.5, 'grass': 2, 'steel': 0, 'bug': 2, 'rock': 2, 'water': 0.5}, 
            'flying': {'fire': 2, 'flying': 0.5, 'electric': 0.5, 'grass': 0.5, 'steel': 0.5, 'rock': 0, 'water': 2}, 
            'electric': {'ground': 2, 'fairy': 2, 'fire': 0.5, 'flying': 2, 'dragon': 0, 'poison': 0.5, 'grass': 2, 'rock': 2}, 
            'dragon': {'fairy': 0.5, 'fire': 2, 'dark': 2, 'poison': 2, 'grass': 0.5, 'rock': 0.5}, 
            'ghost': {'dark': 2, 'flying': 2, 'ghost': 0.5, 'bug': 0, 'rock': 0}, 
            'poison': {'ground': 0.5, 'fire': 2, 'dark': 0.5, 'flying': 0.5, 'dragon': 0.5, 'ghost': 2, 'steel': 0.5, 'bug': 2, 'rock': 0.5, 'water': 0.5}, 
            'grass': {'ground': 2, 'normal': 2, 'dark': 0.5, 'electric': 0.5, 'dragon': 2, 'poison': 2, 'rock': 0.5}, 
            'steel': {'fighting': 0, 'ghost': 2, 'steel': 2, 'bug': 0.5}, 
            'psychic': {'psychic': 2, 'rock': 0.5, 'water': 0},
            'bug': {'ghost': 2, 'steel': 2, 'bug': 0.5, 'water': 0.5},
            'rock': {'ground': 0.5, 'ice': 0.5, 'fairy': 0.5, 'normal': 2, 'grass': 2, 'rock': 0.5, 'water': 2},
            'water': {'ground': 0.5, 'dark': 2, 'flying': 0.5, 'psychic': 2, 'bug': 2, 'rock': 0.5}
        }

        self.ui.Calculate_pushButton.clicked.connect(self.calculate_effectiveness)

    def calculate_effectiveness(self):
        move_type = self.ui.Type_comboBox.currentText().lower()

        super_effective = []
        neutral = []
        immune = []
        resisted = []

        all_types = list(self.effectiveness_chart.keys())

        for type1 in all_types:
            for type2 in all_types:
                if type1 == type2:
                    multiplier = self.effectiveness_chart.get(move_type, {}).get(type1, 1)
                else:
                    multiplier1 = self.effectiveness_chart.get(move_type, {}).get(type1, 1)
                    multiplier2 = self.effectiveness_chart.get(move_type, {}).get(type2, 1)
                    
                    multiplier = multiplier1 * multiplier2

                if multiplier in [2, 4]:
                    super_effective.append(f"{type1}/{type2}: {multiplier}")
                elif multiplier == 1:
                    neutral.append(f"{type1}/{type2}: {multiplier}")
                elif multiplier == 0:
                    immune.append(f"{type1}/{type2}: {multiplier}")
                elif multiplier in [0.5, 0.25]:
                    resisted.append(f"{type1}/{type2}: {multiplier}")
                else:
                    raise ValueError(f"Invalid multiplier {multiplier} for types ({type1}, {type2}) and move type '{move_type}'.")

        self.ui.Super_textEdit.setPlainText("\n".join(super_effective))
        self.ui.Neutral_textEdit.setPlainText("\n".join(neutral))
        self.ui.Immune_textEdit.setPlainText("\n".join(immune))
        self.ui.Resisted_textEdit.setPlainText("\n".join(resisted))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MoveEffectivenessCalc()
    window.show()
    sys.exit(app.exec_())
