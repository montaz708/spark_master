import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.igext as IG

pc = portal.Context()
request = rspec.Request()


params = pc.bindParameters()
tourDescription = \
"""
Testing Spark cluster environment
"""

#
# Setup the Tour info with the above description and instructions.
#
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)

node = request.RawPC("head")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"

node.addService(rspec.Execute(shell="sh",
                                command="sudo bash /local/repository/install_spark.sh"))
node.addService(rspec.Execute(shell="/bin/sh",
                                command="sudo apt-get update -y"))
node.addService(rspec.Execute(shell="/bin/sh",
                                command="sudo apt-get install -y openjdk-8-jdk"))
node.addService(rspec.Execute(shell="/bin/sh",
                                command="export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/")) 
node.addService(rspec.Execute(shell="/bin/sh",
                                command="sudo /opt/spark-2.4.1-bin-hadoop2.7/sbin/start-master.sh"))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec(request)
