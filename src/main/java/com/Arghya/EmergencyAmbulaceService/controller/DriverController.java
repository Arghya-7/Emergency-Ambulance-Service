package com.Arghya.EmergencyAmbulaceService.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.Arghya.EmergencyAmbulaceService.Entity.Driver;
import com.Arghya.EmergencyAmbulaceService.service.DriverServices;

@RestController
//@ComponentScan ({"com.Arghya.EmergecyAmbulanceService.service.DriverServices", "com.Arghya.EmergecyAmbulanceService.service.UserServices"})
public class DriverController 
{
	@Autowired
	DriverServices driverServices;
	
	@GetMapping("/")
	public String homePage()
	{
		return "<h1>Hello Driver</h1>";
	}
	@GetMapping("/display")
	public List<Driver> displayAllDriver()
	{
		return driverServices.displayAll();
	}
	@PostMapping("/driver/register")
	public Driver registerDriver(@RequestBody Driver driver)
	{
		return driverServices.registerDriver(driver);
	}
	
	@PutMapping("/driver/go-online")
	public Driver goOnline(@RequestBody Driver driver)
	{
		return driverServices.updateDetails(driver);
	}
	
	@PutMapping("/driver/go-offline")
	public Driver goOffline(@RequestBody Driver driver)
	{
		return driverServices.goOffline(driver);
	}
	
	@GetMapping("/user/display-by-pincode/{pincode}")
	public List<Driver> findAllDriversByPincode(@PathVariable String pincode)
	{
//		System.out.println(pincode);
		return driverServices.findAllActive(pincode);
	}
	@GetMapping("/user/display-by-loc-and-pincode/{location}/{pincode}")
	public List<Driver> findByPincodeAndActiveAndLocation(@PathVariable String pincode,@PathVariable String location)
	{
		location = location.toUpperCase();
		return driverServices.findAllActiveWithLocaltion(pincode, location);
	}
}
