namespace PluralKit.Core;

public class GuildConfig
{
    public ulong Id { get; }
    public ulong? LogChannel { get; }
    public ulong[] LogBlacklist { get; }
    public ulong[] Blacklist { get; }
    
    public bool SettingProxyLock { get; }
    
    public ulong[] ProxyRole { get; }
    public bool LogCleanupEnabled { get; }
}