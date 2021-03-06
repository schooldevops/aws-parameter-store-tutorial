package com.schooldevops.ssm.parameterstore;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Component;

@Component
@SpringBootApplication
public class ParameterStoreApplication implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(ParameterStoreApplication.class, args);
	}

	@Value("${dbname}")
	private String dbname;

	@Value("${test.value}")
	private String testValue;

	@Value("${api.password}")
	private String api_password;

	@Override
	public void run(String... args) throws Exception {
		System.out.println("DBName: " + dbname + " : " + testValue + " apiPassword: " + api_password);
	}
}
