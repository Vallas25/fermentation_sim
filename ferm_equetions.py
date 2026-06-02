class equations:
    def __init__(self, biomass: int | float,
                substrate:int | float, 
                vollume: int | float, 
                mu_max: int | float = 0.5, 
                dt: int | float = 5, 
                product: int | float = 0):
        self.biomass = biomass
        self.substrate = substrate
        self.product = product
        self.vollume = vollume
        self.mu_max = mu_max
        self.dt = dt
        self.mu = mu_max
        self.half_saturation_constant = 5
        self.biomass_substrate_constant = 5
        self.product_yeald_biomass_constant = 5
    

    def growth_speed(self):
        self.mu = self.mu_max*(self.substrate/(self.half_saturation_constant+self.substrate))
    
    def new_biomass(self):
        self.biomass =self.biomass + (self.dt * self.mu * self.biomass)
    
    def new_substrate(self):
        self.substrate = self.substrate - ((1/self.biomass_substrate_constant)*self.mu*self.biomass)
    
    def update(self):
        self.growth_speed()
        self.new_biomass()
        self.new_substrate()


def main():
    time_current = 0
    fermentation = equations(
        biomass=0.2,
        substrate=10,
        vollume=3,
        mu_max= 0.5,
        dt = 5,
        product= 0)
    
    while time_current < 100 and fermentation.substrate > 0:
        print(f"at: {time_current} min \n biomass: {fermentation.biomass}\n substrate: {fermentation.substrate}")
        fermentation.update()
        time_current += 5

if __name__ == "__main__":
    main()