import hudson.security.*
import jenkins.model.*

def instance = Jenkins.getInstance()

// Set up Jenkins security realm (e.g., Jenkins' own user database)
def hudsonRealm = new HudsonPrivateSecurityRealm(false)
hudsonRealm.createAccount('admin', 'admin_password')
instance.setSecurityRealm(hudsonRealm)

// Set up authorization strategy (e.g., full control for admin user)
def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
strategy.setAllowAnonymousRead(false)
instance.setAuthorizationStrategy(strategy)

instance.save()
