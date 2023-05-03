class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/micros/projects/OSTrack-main/result'  # Base directory for saving network checkpoints.
        # self.workspace_dir + '/pretrained_networks/'
        self.lasot_dir = '/mnt/first/hushiyu/SOT/LaSOT/data'
        self.got10k_dir = '/mnt/first/hushiyu/SOT/GOT-10k/data'
        self.BioDrone_dir = '/mnt/second/hushiyu/UAV/BioDrone'
        self.trackingnet_dir = '/mnt/second/wangyipei/trackingnet'
        self.coco_dir = '/mnt/second/wangyipei/coco_root'
        self.otb_dir = '/mnt/first/hushiyu/SOT/OTB/data'
        self.vot_dir = ''
        self.imagenet_dir = ''
        self.imagenetdet_dir = ''

        #
        self.lasotSOI_dir = '/mnt/first/hushiyu/SOT/LaSOT/data'  # '/mnt/second/wangyipei/SOI/data/lasot/data'
        self.got10k_dir = '/mnt/first/hushiyu/SOT/GOT-10k/data'  # '/mnt/second/wangyipei/SOI/GOT-10k/data'

    def find_root_dir(self, dataset_str=None):
        if dataset_str is None:
            print('no dataset choose')
            return None
        elif dataset_str == 'lasot':
            return self.lasot_dir
        elif dataset_str == 'got10k':
            return self.got10k_dir
        elif dataset_str == 'coco':
            return self.coco_dir
        elif dataset_str == 'otb':
            return self.otb_dir
        elif dataset_str == 'lasotSOI':
            return self.lasotSOI_dir
        elif dataset_str == 'got10kSOI':
            return self.lasotSOI_dir
