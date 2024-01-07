package com.Arghya.EmergencyAmbulaceService.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.Arghya.EmergencyAmbulaceService.Entity.Driver;

@Repository
public interface ServiceRepository extends JpaRepository<Driver,String>{
	List<Driver> findByPincodeAndActive(String pincode,boolean active);
	List<Driver> findByPincodeAndActiveAndLocation(String pincode,boolean active,String location);

}
