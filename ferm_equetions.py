from START_VALUES import *

class equations:
    def __init__(self, biomass: int | float,
                substrate_concentration :int | float, 
                volume: int | float,
                max_time: int | float, 
                feed_rate: int | float,
                feed_concentration: int | float,
                max_volume: int | float,
                trigger_condition: str,
                trigger_value: int | float,
                mu_max: int | float = 0.5, 
                dt: int | float = 5,
                is_fedbatch: bool = False, 
                product: int | float = 0):
        self.biomass = biomass
        self.volume = volume
        self.substrate_concentration = substrate_concentration
        self.substrate = substrate_concentration * self.volume
        self.product = product
        self.mu_max = mu_max/60
        self.max_time = max_time
        self.dt = dt
        self.mu = mu_max
        self.feed_rate = feed_rate/1000
        self.feed_concentration = feed_concentration
        self.max_volume = max_volume
        self.is_fedbatch = is_fedbatch
        self.trigger_condition = trigger_condition
        self.trigger_value = trigger_value
        self.__trigger = False
        self.half_saturation_constant = 0.1
        self.time_current = 0
        self.biomass_substrate_constant = 5
        self.product_yeald_biomass_constant = 5
        self.time_steps = []
        self.biomass_steps = []
        self.mu_steps = []
        self.substrate_concentration_steps = []
        self.volume_steps =[]
    

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
        self.substrate_concentration = total_substrate / self.volume
    
    def new_volume(self):
        self.volume += self.feed_rate
        self.substrate += self.feed_concentration * self.feed_rate
        self.substrate_concentration = self.substrate_concentration/self.volume
    
    def initialise(self):
        if self.is_fedbatch and self.volume >= self.max_volume:
            raise Exception("Max vollume should be greater than start vollume")
        self.__trigger = False
        self.time_current = 0
        self.time_steps= []
        self.mu_steps = []
        self.biomass_steps= []
        self.substrate_concentration_steps = []
        self.volume_steps = []
    
    def trigger_is_met(self):
        if self.__trigger == False:
            if self.trigger_condition == "OD" and self.biomass > self.trigger_value:
                self.__trigger = True
            if self.trigger_condition == "Substrate" and self.substrate < self.trigger_value:
                self.__trigger = True
            if self.trigger_condition == "Time" and self.time_current > self.trigger_value:
                self.trigger_condition = True
    
    def update(self):
        self.trigger_is_met()
        self.growth_speed()
        self.new_biomass()
        self.new_substrate()
        if self.volume < self.max_volume and self.__trigger == True and self.is_fedbatch == True:
            self.new_volume()
    
    def run(self):
        self.initialise()
        
        while self.time_current < self.max_time:
            self.time_steps.append(self.time_current)
            self.mu_steps.append(self.mu)
            self.biomass_steps.append(self.biomass)
            self.substrate_concentration_steps.append(self.substrate_concentration)
            self.volume_steps.append(self.volume)
            self.update()
            self.time_current += self.dt


def main():
    fermentation = equations(
        biomass=0.4,
        substrate_concentration=10,
        volume=3,
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