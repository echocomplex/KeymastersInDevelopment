#include "SCAMGuard.hpp"

SCAMGuard::SCAMGuard (std::string email, std::string password, std::string server, int port) {
    this->curl = curl_easy_init();
    curl_easy_setopt(this->curl, CURLOPT_USERNAME, email.c_str());
    curl_easy_setopt(this->curl, CURLOPT_PASSWORD, password.c_str());
    std::string serverToCurl = "imaps//" + server + ":" + std::to_string(port);
    curl_easy_setopt(this->curl, CURLOPT_URL, serverToCurl.c_str());
}