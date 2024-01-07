package com.Arghya.EmergencyAmbulaceService.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.Arghya.EmergencyAmbulaceService.Entity.Driver;
import com.Arghya.EmergencyAmbulaceService.repository.ServiceRepository;

@Service
public class DriverServices implements AllServices{
	
	@Autowired
	ServiceRepository serviceRepository;

	@Override
	public Driver registerDriver(Driver driver)
	{
		// TODO Auto-generated method stub
		java.util.Optional<Driver> drivers = serviceRepository.findById(driver.getPhone());
		if(drivers.isEmpty()==false)
		{
			return null;
		}
		return serviceRepository.save(driver);
	}

	public boolean checkPassword(Driver driver,Driver request)
	{
		if(driver.getPassword().equals(request.getPassword()))
		{
			return true;
		}
		return false;
	}
//	For going online
	public Driver updateDetails(Driver driver) {
		// TODO Auto-generated method stub
		java.util.Optional<Driver> drivers = serviceRepository.findById(driver.getPhone());
		
		if(drivers.isEmpty() == true)
		{
			return null;
		}
		else
		{
			Driver oldDriverObject = drivers.get();
			if(checkPassword(oldDriverObject,driver))
			{
				oldDriverObject.setActive(true);
				oldDriverObject.setLocation(driver.getLocation());
				oldDriverObject.setPincode(driver.getPincode());
				serviceRepository.save(oldDriverObject);
				return oldDriverObject;
			}
			else
			{
				return null;
			}
		}
	}

	public Driver goOffline(Driver driver) {
		// TODO Auto-generated method stub
		java.util.Optional<Driver> drivers = serviceRepository.findById(driver.getPhone());
		
		if(drivers.isEmpty() == true)
		{
			return null;
		}
		else
		{
			Driver oldDriverObject = drivers.get();
			if(checkPassword(oldDriverObject,driver))
			{
				oldDriverObject.setActive(false);
				oldDriverObject.setLocation(driver.getLocation());
				oldDriverObject.setPincode(driver.getPincode());
				serviceRepository.save(oldDriverObject);
				return oldDriverObject;
			}
			else
			{
				return null;
			}
		}
	}

	public List<Driver> displayAll() {
		// TODO Auto-generated method stub
		return serviceRepository.findAll();
	}
	
	public List<Driver> findAllActive(String pincode) {
		// TODO Auto-generated method stub
		return serviceRepository.findByPincodeAndActive(pincode, true);
	}
	public List<Driver> findAllActiveWithLocaltion(String pincode,String location) {
		// TODO Auto-generated method stub
		return serviceRepository.findByPincodeAndActiveAndLocation(pincode, true,location);
	}
}
