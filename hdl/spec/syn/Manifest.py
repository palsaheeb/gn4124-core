target = "xilinx"
action = "synthesis"

syn_device = "xc6slx45t"
syn_grade = "-3"
syn_package = "fgg484"
syn_top = "spec_gn4124_test"
syn_project = "spec_gn4124_test.xise"

files = ["../spec_gn4124_test.ucf"]

modules = { "local" : ["../rtl",
                       "../../common/rtl",
                       "../../gn4124core/rtl"],
            "git" : "git://ohwr.org/hdl-core-lib/general-cores.git::master"}

fetchto = "../ip_cores"

