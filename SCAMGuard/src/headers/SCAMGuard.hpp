#ifndef KEYMASTERS_SCAMGUARD_HPP
#define KEYMASTERS_SCAMGUARD_HPP

#include <curl/curl.h>
#include <string>

class SCAMGuard {
private:
    CURL *curl;
    char *imapServer;
    char *smtpServer;

public:
    SCAMGuard (std::string email, std::string password, std::string server, int port);
    SCAMGuard (const SCAMGuard *unit);
    bool startGuard ();
};

#endif