package com.Arghya.EmergencyAmbulaceService;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
//@ComponentScan ({"com.Arghya.EmergecyAmbulanceService.service", "com.Arghya.EmergecyAmbulanceService.service.UserServices"})
public class EmergencyAmbulaceServiceApplication {

	public static void main(String[] args) 
	{	
		SpringApplication.run(EmergencyAmbulaceServiceApplication.class, args);
	}

}
