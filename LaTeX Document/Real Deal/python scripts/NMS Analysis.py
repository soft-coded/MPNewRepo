file_name = "shibuya_100frames.mp4"

object_thresholds = [0.25,0.5,0.75,0.85,0.95]
nms_thresholds = np.linspace(0.01,0.025, 30)

plt.figure("NMS vs Performance",figsize=(15,15))
plt.xlabel("NMS Threshold")
plt.ylabel("Performace Ratio ( Bad Frames / Total Frames)")
value = 1

for object_threshold in object_thresholds:
    performance_ratios = []
    for nms_threshold in nms_thresholds:
        clear_output()
        print(f"{value}/{5*30}")
        performance_ratios.append(performance_ratio(object_threshold,nms_threshold,file_name))
        value = value+1
    plt.plot(nms_thresholds,performance_ratios,linestyle = '-',marker = 'o',label = f"Obj_Thr = {object_threshold}")

plt.legend(loc = "best")
plt.savefig("NMS vs Performance")
plt.show()