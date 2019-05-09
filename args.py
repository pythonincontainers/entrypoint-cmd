import sys, signal, time, psutil

signames = ['Zero!','SIGHUP','SIGINT','SIGQUIT','SIGILL','SIGTRAP','SIGABRT','SIGBUS','SIGFPE','SIGKILL','SIGUSR1','SIGSEGV','SIGUSR2','SIGPIPE','SIGALRM','SIGTERM','SIGSTKFLT','SIGCHLD','SIGCONT','SIGSTOP','SIGTSTP','SIGTTIN','SIGTTOU','SIGURG','SIGXCPU','SIGXFSZ','SIGVTALRM','SIGPROF','SIGWINCH','SIGIO','SIGPWR','SIGSYS']

def handler(signal, frame):
    print('Signal received: ', signames[signal])
    return

if __name__ == '__main__':
    print("This process PID: ", psutil.Process().pid)
    print("This process command line: ", psutil.Process().cmdline())
    print("List of all processes in current Container:")

    for proc in psutil.process_iter(attrs=['pid','ppid','cmdline']):
        print("PID=",proc.info['pid']," PPID=",proc.info['ppid']," CMDLINE=",proc.info['cmdline'])

    if sys.argv[1] == 'signals':
        signals_allowed = set(signal.Signals) - {signal.SIGKILL, signal.SIGSTOP}
        for sig in signals_allowed:
            signal.signal(sig, handler)
        print("Waiting for signals, please send some :)")
        while True:
            signal.pause()
