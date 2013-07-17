#include <ros/ros.h>
#include <std_msgs/Int32.h>

class Node
{
private:
  ros::NodeHandle _nh;
  ros::Subscriber _sub;
  ros::Publisher _pub;

public:
  Node()
  {
    _sub = _nh.subscribe("input topic", 1000, &Node::callback, this);
    _pub = _nh.advertise<std_msgs::Int32>("output topic", 1000);
  }

  void callback(const std_msgs::Int32& data)
  {
  }
};

int main(int argc, char* argv[])
{
  ros::init(argc, argv, "node");

  Node node;

  ros::spin();
}
