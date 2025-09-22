from ai.engine import SERAIEngine

class TeleportSimulator:
    def __init__(self, engine):
        self.engine = engine
        self.tp_data = engine.summarize_tp_stages()

    def run_basic_simulation(self):
        results = {}
        for stage, info in self.tp_data.items():
            # Simplified feasibility logic
            if stage in ["TP-001", "TP-002"]:
                results[stage] = "Feasible"
            elif stage in ["TP-003", "TP-004"]:
                results[stage] = "Experimental"
            else:
                results[stage] = "Infeasible"
        return results

if __name__ == "__main__":
    engine = SERAIEngine("../extensions/Aura.xlsx")
    simulator = TeleportSimulator(engine)
    sim_results = simulator.run_basic_simulation()
    for stage, outcome in sim_results.items():
        print(f"{stage}: {outcome}")
