CREATE DATABASE privacy_authentication_system;

USE privacy_authentication_system;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('user', 'admin', 'TPA') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE files (
    file_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    filename VARCHAR(255) NOT NULL,
    file_hash VARCHAR(255) UNIQUE NOT NULL,
    file_size INT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('active', 'archived', 'deleted') DEFAULT 'active',
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE access_requests (
    request_id INT PRIMARY KEY AUTO_INCREMENT,
    file_id INT,
    requester_id INT,
    owner_id INT,
    status ENUM('pending', 'approved', 'denied') DEFAULT 'pending',
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    approval_date TIMESTAMP NULL,
    FOREIGN KEY (file_id) REFERENCES files(file_id) ON DELETE CASCADE,
    FOREIGN KEY (requester_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE third_party_auditor (
    audit_id INT PRIMARY KEY AUTO_INCREMENT,
    request_id INT,
    tpa_id INT,
    verification_status ENUM('verified', 'rejected') DEFAULT 'verified',
    verification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES access_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (tpa_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE encryption_keys (
    key_id INT PRIMARY KEY AUTO_INCREMENT,
    file_id INT,
    owner_id INT,
    encrypted_key VARCHAR(512) NOT NULL,
    issued_to INT,
    issued_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (file_id) REFERENCES files(file_id) ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (issued_to) REFERENCES users(user_id) ON DELETE CASCADE
);
