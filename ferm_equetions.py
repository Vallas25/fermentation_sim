class equations:
    def __init__(self, biomass: int | float,
                substrate_concentration :int | float, 
                vollume: int | float,
                max_time: int | float, 
                mu_max: int | float = 0.5, 
                dt: int | float = 5, 
                product: int | float = 0):
        self.biomass = biomass
        self.substrate_concentration = substrate_concentration
        self.substrate = substrate_concentration * vollume
        self.product = product
        self.vollume = vollume
        self.mu_max = mu_max/60
        self.max_time = max_time
        self.dt = dt
        self.mu = mu_max
        self.half_saturation_constant = 0.1
        self.time_current = 0
        self.biomass_substrate_constant = 5
        self.product_yeald_biomass_constant = 5
        self.time_steps = []
        self.biomass_steps = []
        self.mu_steps = []
        self.substrate_concentration_steps = []
    

    def growth_speed(self):
        if self.substrate <= 0:
            self.mu = 0
        else:
            self.mu = self.mu_max*(self.substrate/(self.half_saturation_constant+self.substrate))
    
    def new_biomass(self):
        self.biomass =self.biomass + (self.dt * self.mu * self.biomass)
    
    def new_substrate(self):
        if self.substrate <= 0:
            self.substrate = 0
        total_substrate = self.substrate - ((1/self.biomass_substrate_constant)*self.mu*self.biomass)
        self.substrate = total_substrate
        self.substrate_concentration = total_substrate / self.vollume
    
    def update(self):
        self.growth_speed()
        self.new_biomass()
        self.new_substrate()
    
    def run(self):
        self.time_current = 0
        self.time_steps= []
        self.mu_steps = []
        self.biomass_steps= []
        self.substrate_concentration_steps = []
        
        while self.time_current < self.max_time:
            self.time_steps.append(self.time_current)
            self.mu_steps.append(self.mu)
            self.biomass_steps.append(self.biomass)
            self.substrate_concentration_steps.append(self.substrate_concentration)
            self.update()
            self.time_current += self.dt


def main():
    fermentation = equations(
        biomass=0.4,
        substrate_concentration=10,
        vollume=3,
        mu_max= 0.5,
        dt = 1,
        max_time=10,
        product= 0)
    
    fermentation.run()

    print(fermentation.time_steps)
    print(fermentation.mu_steps)
    print(fermentation.substrate_concentration_steps)

if __name__ == "__main__":
    main()