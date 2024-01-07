package com.Arghya.EmergencyAmbulaceService.Entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Driver {
	@GeneratedValue(strategy = GenerationType.AUTO)
	private int id;
	private boolean active;
	private String name;
	private String pincode;
	private String location;
	@Id
	private String phone;
	private String password;
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public boolean isActive() {
		return active;
	}
	public void setActive(boolean active) {
		this.active = active;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPincode() {
		return pincode;
	}
	public void setPincode(String pincode) {
		this.pincode = pincode;
	}
	public String getLocation() {
		if(location == null)
		{
			return null;
		}
		return location.toUpperCase();
	}
	public void setLocation(String location) {
		if(location == null)
		{
			this.location = null;
		}
		else
		{
			this.location = location.toUpperCase();
		}
	}
	public Driver(int id, boolean active, String name, String pincode, String location, String phone, String password) {
		super();
		this.id = id;
		this.active = active;
		this.name = name;
		this.pincode = pincode;
		this.location = location.toUpperCase();
		this.phone = phone;
		this.password = password;
	}
	public Driver()
	{
		
	}
}
