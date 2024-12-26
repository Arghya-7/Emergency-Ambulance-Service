package com.Arghya.EmergencyAmbulaceService;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
//@ComponentScan ({"com.Arghya.EmergecyAmbulanceService.service", "com.Arghya.EmergecyAmbulanceService.service.UserServices"})
public class EmergencyAmbulaceServiceApplication {
	public static final Logger logger = LoggerFactory.getLogger(EmergencyAmbulaceServiceApplication.class);
	public static void main(String[] args) 
	{	
		SpringApplication.run(EmergencyAmbulaceServiceApplication.class, args);
		logger.info("Application started successfully");
	}
}

