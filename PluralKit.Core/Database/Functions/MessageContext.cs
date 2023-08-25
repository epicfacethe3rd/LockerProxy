#nullable enable

using NodaTime;

namespace PluralKit.Core;

/// <summary>
/// Model for the `message_context` PL/pgSQL function in `functions.sql`
/// </summary>
public class MessageContext
{
    public SystemId? SystemId { get; }

    /// <summary>
    /// Whether a system is being deleted (no actions should be taken, or commands ran)
    /// </summary>
    public ulong? LogChannel { get; }
    public bool InBlacklist { get; }
    public bool IsProxyLocked { get; }
    public string? ProxyRole { get; } // Might need to be ulong and not a string, unsure
    public bool InLogBlacklist { get; }
    public bool LogCleanupEnabled { get; }
    public bool ProxyEnabled { get; }
    public SwitchId? LastSwitch { get; }
    public MemberId[] LastSwitchMembers { get; } = new MemberId[0];
    public Instant? LastSwitchTimestamp { get; }
    public string? SystemTag { get; }
    public string? SystemGuildTag { get; }
    public bool TagEnabled { get; }
    public string? SystemAvatar { get; }
    public string? SystemGuildAvatar { get; }
    public bool AllowAutoproxy { get; }
    public int? LatchTimeout { get; }
    public bool CaseSensitiveProxyTags { get; }
    public bool ProxyErrorMessageEnabled { get; }
}